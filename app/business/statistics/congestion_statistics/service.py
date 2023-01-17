import os
from datetime import date

import pandas as pd

from business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from business.preprocessing.utils.utils import get_center_coordinate


def service():
    area_map = pd.read_csv(PATH_격자_집계구_MAP, encoding=UTF_8)

    report_df = pd.read_csv(PATH_112신고접수정보_ORIGIN)
    report_df = report_df.astype({'TIME': 'str'})
    report_df['NEW_TIME'] = report_df['TIME'].apply(fill_zero)

    for path in MONTH_PATH_LIST:
        for item in os.listdir(path):

            print("파일 : [", item, "] 의 혼잡도를 계산 합니다")
            life_population_df = pd.read_csv(path + item, encoding=EUC_KR)

            save_path = PATH_혼잡도_RESULT + item.split('.')[0][-8:] + ".csv"

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
                sub_report_df = get_center_coordinate(sub_report_df, 'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                                                      'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')
                sub_report_df = count_point_in_polygon(True, PATH_격자_MAP, CP_949, '격자고유번호', sub_report_df, save_path,
                                                       'x', 'y', EPSG_4326)

                concat_report_time_lift_population_map_df = pd.merge(grid_time_life_population_map, sub_report_df,
                                                                     on='격자고유번호', how='inner')

                dfs.append(make_df(concat_report_time_lift_population_map_df, day_month_year,weekday, time))

            pd.concat(dfs).to_csv(save_path, index=False)



#최종적으로 산출될 df
def make_df(concat_report_time_lift_population_map_df, day_month_year, weekday, time):
    columns = ['기준일','요일','시간대','위험방지 신고건수','생활인구','격자고유번호']
    statistics_df = pd.DataFrame(columns=columns)
    statistics_df['위험방지 신고건수'] = concat_report_time_lift_population_map_df['count']
    statistics_df['생활인구'] = concat_report_time_lift_population_map_df['총생활인구수'] / concat_report_time_lift_population_map_df['duplicate']
    statistics_df['격자고유번호'] = concat_report_time_lift_population_map_df['격자고유번호']
    statistics_df['기준일'] = day_month_year
    statistics_df['요일'] = weekday
    statistics_df['시간대'] = time + "시"

    return statistics_df


def fill_zero(values):
    return values.zfill(6)[0:2]


def get_weekday(target):
    days = ['월', '화', '수', '목', '금', '토', '일']
    return days[date(int(target[0:4]), int(target[4:6]), int(target[6:8])).weekday()]
