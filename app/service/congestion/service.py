# -*- coding: utf-8 -*-

import pandas as pd
from app.utils.constants import *

def service(grid_area_map, area_map, life_population, report):         # create congestion data by day
    for time in life_population.get_hour_list():        # loop in time (0 to 23)
        grid_time_life_population_map = pd.merge(grid_area_map,
                                                 life_population.get_life_population_filtered_hour(
                                                     time).life_population,
                                                 left_on='TOT_REG_CD',
                                                 right_on='집계구코드', how='inner')

        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        count_point_df = count_point_in_polygon(area_map, 'TOT_REG_CD',
                                                report.get_report_filtered_hour(time).report,
                                                'x', 'y', EPSG_4326, False)

        grid_time_life_population_map['TOT_REG_CD']= grid_time_life_population_map['TOT_REG_CD'].astype(str)
        count_point_df['TOT_REG_CD'] = count_point_df['TOT_REG_CD'].astype(str)

        concat_life_population_report_df = pd.merge(grid_time_life_population_map, count_point_df,
                                                    on='TOT_REG_CD', how='inner')        # concat life population and report

        concat_life_population_report_df=concat_life_population_report_df.drop_duplicates(['TOT_REG_CD'])
        concat_life_population_report_df= pd.merge(concat_life_population_report_df,area_map,on='TOT_REG_CD', how='left')
        insert_data(make_df(concat_life_population_report_df, life_population, time))


def make_df(df, life_population, time):
    new_df = pd.DataFrame()
    new_df['report_count'] = df['count'].map(lambda x: int(x))
    new_df['life_population'] = round(df['총생활인구수'], 3)
    new_df['tot_reg_cd']= df['TOT_REG_CD']
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
