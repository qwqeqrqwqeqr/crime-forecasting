# -*- coding: utf-8 -*-

import pandas as pd
from app.utils.constants import *


def service(area_congestion_map, life_population, report):  # create congestion data by day
    for time in life_population.get_hour_list():  # loop in time (0 to 23)
        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        count_report_df = count_point_in_polygon(area_congestion_map, 'TOT_REG_CD',
                                                report.get_report_filtered_hour(time).report,
                                                'x', 'y', EPSG_4326, False)  # 집계구 마다의 신고 건수 추출

        filtered_life_population_df = life_population.get_life_population_filtered_hour(time).life_population       # 특정 시간대에 대한 집계구를 추출

        filtered_life_population_df['집계구코드'] = filtered_life_population_df['집계구코드'].astype(str)       # 타입 변경
        count_report_df['TOT_REG_CD'] = count_report_df['TOT_REG_CD'].astype(str)       # 타입 변경

        concat_life_population_report_df = pd.merge(filtered_life_population_df, count_report_df, left_on='집계구코드',
                                                    right_on='TOT_REG_CD',
                                                    how='inner')  # merge life population and report

        concat_life_population_report_df = concat_life_population_report_df.drop_duplicates(['TOT_REG_CD'])     # 후처리 작업
        concat_life_population_report_df = pd.merge(concat_life_population_report_df, area_congestion_map,      # 위에 전처리 과정에서 사라진 혼잡지역 컬럼 연결
                                                    on='TOT_REG_CD', how='left')
        insert_data(concat_sub_data(concat_life_population_report_df, life_population, time))


def concat_sub_data(df, life_population, time):     # 부가적인 데이터 연결
    new_df = pd.DataFrame()
    new_df['report_count'] = df['count'].map(lambda x: int(x))
    new_df['life_population'] = round(df['총생활인구수'], 3)
    new_df['tot_reg_cd'] = df['TOT_REG_CD']
    new_df['name'] = df['hotspotNm']
    new_df.insert(0, 'day_month_year', str(life_population.day.iloc[0]))
    new_df.insert(0, 'weekday', str(life_population.weekday.iloc[0]))
    new_df.insert(0, 'hour', str(time) + "시")

    return new_df


def insert_data(df):  # insert in DB
    insert_list = []
    for idx, row in df.iterrows():
        from app.service.congestion import to_insert_list
        insert_list.append(to_insert_list(row))  # change format to insert in DB

    from app.database.query.congestion import insert_congestion
    insert_congestion(insert_list)
