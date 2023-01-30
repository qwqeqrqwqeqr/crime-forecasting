# -*- coding: utf-8 -*-

import pandas as pd

from app.utils.constants import *


def service(grid_area_map, grid_congestion_map, grid_map, life_population, report):
    for time in life_population.get_hour_list():
        # 집계구 별 격자랑 매핑
        grid_time_life_population_map = pd.merge(grid_area_map,
                                                 life_population.get_life_population_filtered_hour(time).life_population,
                                                 left_on='TOT_REG_CD',
                                                 right_on='집계구코드', how='inner')

        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        count_point_df = count_point_in_polygon(grid_map.grid_map, '격자고유번호',
                                                report.get_report_filtered_hour(time).report,
                                                'x', 'y', EPSG_4326, False)

        concat_life_population_report_df = pd.merge(grid_time_life_population_map, count_point_df,
                             on='격자고유번호', how='inner')
        concat_df = pd.merge(grid_congestion_map,concat_life_population_report_df, on='격자고유번호', how='inner')

        insert_data(make_df(concat_df,life_population,time))


# 최종적으로 산출될 df
def make_df(df,life_population,time):
    new_df = pd.DataFrame()
    new_df['report_count'] = df['count'].map(lambda x: int(x))
    new_df['life_population'] = round((df['총생활인구수'] / df['duplicate']),3)
    new_df['grid_number'] = df['격자고유번호'].map(lambda x: x[-6:])
    new_df['name'] = df['혼잡지역']
    new_df.insert(0,'day_month_year',str(life_population.day.iloc[0]))
    new_df.insert(0, 'weekday', str(life_population.weekday.iloc[0]))
    new_df.insert(0, 'hour', str(time) + "시")

    return new_df


def insert_data(df):
    insert_list = []
    for idx, row in df.iterrows():
        from app.service.congestion import to_insert_list
        insert_list.append(to_insert_list(row))

    from app.database.query.congestion import insert_congestion
    insert_congestion(insert_list)
