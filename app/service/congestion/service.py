import os

import pandas as pd

from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from app.business.preprocessing.utils.utils import get_weekday, get_center_coordinate
from app.database.query.congestion import insert_congestion
from app.utils.constants import *


def service(area_map, grid_map, origin_df):
    origin_df = origin_df.astype({'TIME': 'str'})
    origin_df['NEW_TIME'] = origin_df['TIME'].apply(fill_zero)

    for path in MONTH_PATH_LIST:
        for item in os.listdir(path):

            print("파일 : [", item, "] 의 혼잡도를 계산 합니다")
            life_population_df = pd.read_csv(path + item, encoding=EUC_KR)

            dfs = []
            day_month_year = item.split('.')[0][-8:]
            weekday = get_weekday(day_month_year)

            for t in range(0, 24):
                time = str(t).zfill(2)

                print("--", time, "시의 혼잡도를 계산 합니다.")
                # 시간대 별로 생활인구를 분할
                time_condition = life_population_df['시간대구분'] == t
                time_life_population_df = life_population_df[time_condition]

                # 집계구 별 격자랑 매핑
                grid_time_life_population_map = pd.merge(area_map, time_life_population_df, left_on='TOT_REG_CD',
                                                         right_on='집계구코드', how='inner')

                # 일별 시간대별로 112신고건수 분리
                sub_report_df = origin_df[(origin_df['NEW_TIME'] == time)]
                sub_report_df = sub_report_df[origin_df['DAY'] == int(day_month_year)]
                sub_report_df = count_point_in_polygon(grid_map, '격자고유번호', sub_report_df, 'x', 'y', EPSG_4326, False)

                concat_report_time_lift_population_map_df = pd.merge(grid_time_life_population_map, sub_report_df,
                                                                     on='격자고유번호', how='inner')

                dfs.append(make_df(concat_report_time_lift_population_map_df, day_month_year, weekday, time))
            insert_data(pd.concat(dfs))


# 최종적으로 산출될 df
def make_df(concat_report_time_lift_population_map_df, day_month_year, weekday, time):
    columns = ['report_count', 'life_population', 'grid_number', 'day_month_year', 'weekday', 'hour']
    statistics_df = pd.DataFrame(columns=columns)
    statistics_df['report_count'] = concat_report_time_lift_population_map_df['count']
    statistics_df['life_population'] = concat_report_time_lift_population_map_df['총생활인구수'] / \
                                       concat_report_time_lift_population_map_df['duplicate']
    statistics_df['grid_number'] = concat_report_time_lift_population_map_df['격자고유번호']
    statistics_df['day_month_year'] = day_month_year
    statistics_df['weekday'] = weekday
    statistics_df['hour'] = time + "시"

    return statistics_df


def fill_zero(values):
    return values.zfill(6)[0:2]


def insert_data(df):
    temp_list = []
    for idx, row in df.iterrows():
        temp_list.append((row['day_month_year'],
                         row['weekday'],
                         row['hour'],
                         row['grid_number'],
                         row['report_count'],
                         row['life_population']))
    insert_congestion(temp_list)
