from pandas import DataFrame
import pandas as pd

from app.service.subway.constants import *
from app.utils.constants import *


def service(area_map, grid_map, report):
    concat_df = DataFrame()
    concat_df['grid_number'] = grid_map.grid_number

    for i in range(len(name_list)):
        concat_df = pd.merge(concat_df,
                             make_df(
                                 area_map, grid_map.grid_map,
                                 report.report,
                                 evt_cl_cd_mask_list(report.report)[i],
                                 end_cd_mask_list(report.report), name_list[i]),
                             on='grid_number', how='inner')
    concat_df = concat_sub_data(report, concat_df)

    insert_data(concat_df)


def make_df(area_map, grid_map, report, evt_cl_cd_mask_list, end_cd_mask_list, name_list):
    new_df = DataFrame()
    for i in range(len(name_list)):
        from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
        count_point_df = count_point_in_polygon(grid_map,
                                                '격자고유번호',
                                                report.loc[evt_cl_cd_mask_list & end_cd_mask_list[i]],
                                                'x', 'y',
                                                EPSG_4326, False)

        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(lambda x: x[-6:])
        new_df['name'] = concat_df['지하철']
    return new_df


def concat_sub_data(report, new_df):
    new_df.insert('weekday', str(report.weekday.iloc[0]))
    new_df.insert('day_month_year', str(report.day.iloc[0]))
    new_df.insert('month', str(report.day.iloc[0])[4:6])
    new_df.insert('year', str(report.day.iloc[0])[0:4])
    return new_df


def insert_data(df):
    temp_list = []
    for idx, row in df.iterrows():
        temp_list.append(get_df_for_insert)

    from app.database.query.subway import insert_subway
    insert_subway(temp_list)
