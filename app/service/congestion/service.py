import os

import pandas as pd

from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from app.business.preprocessing.utils.utils import get_weekday, get_center_coordinate
from app.database.query.congestion import insert_congestion
from app.utils.constants import *


def service(area_map, grid_map, report_df):

    report_df['NEW_TIME'] = report_df.time

    # 디렉터리 개수 만큼 반복이 된다 (현재 기준 12개)  (현재 생활 인구를 월별로 분류 해두었기 때문이다.)
    for path in MONTH_PATH_LIST:
        #디렉터리 안에 있는 파일 만큼 반복한다. 예를 들어, 1월달 디렉터리 일 경우 총 31개가 있음
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
                sub_report_df = report_df[(report_df['NEW_TIME'] == time)]
                sub_report_df = sub_report_df[report_df['DAY'] == int(day_month_year)]
                sub_report_df = count_point_in_polygon(grid_map, '격자고유번호', sub_report_df, 'x', 'y', EPSG_4326, False)

                concat_report_time_lift_population_map_df = pd.merge(grid_time_life_population_map, sub_report_df,
                                                                     on='격자고유번호', how='inner')
                #필터링된 데이터를 바탕으로 df를 만들어낸다.
                dfs.append(make_df(concat_report_time_lift_population_map_df, day_month_year, weekday, time))
            # 만들어낸 df를 db에 삽입한다.
            insert_data(pd.concat(dfs))


# 최종적으로 산출될 df
def make_df(concat_report_time_lift_population_map_df, day_month_year, weekday, time):
    columns = ['report_count', 'life_population', 'grid_number', 'day_month_year', 'weekday', 'hour']
    statistics_df = pd.DataFrame(columns=columns)
    statistics_df['report_count'] = concat_report_time_lift_population_map_df['count']
    statistics_df['life_population'] = concat_report_time_lift_population_map_df['총생활인구수'] / \
                                       concat_report_time_lift_population_map_df['duplicate']
    statistics_df['grid_number'] = concat_report_time_lift_population_map_df['격자고유번호'].map(slice_grid_number)
    statistics_df['day_month_year'] = day_month_year
    statistics_df['weekday'] = weekday
    statistics_df['hour'] = time + "시"

    return statistics_df



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
