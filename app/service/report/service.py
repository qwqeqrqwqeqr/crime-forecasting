# -*- coding: utf-8 -*-


import pandas as pd

from app.service.report import *
from app.utils.constants import *

def service(grid_map, report):
    concat_df = pd.DataFrame()
    concat_df['grid_number'] = grid_map.grid_number

    for i in range(len(name_list)):  # concat filtered evt, cd  df
        concat_df = pd.merge(concat_df,
                             make_df(
                                 grid_map.grid_map,
                                 report.report,
                                 evt_cl_cd_mask_list(report.report)[i],
                                 end_cd_mask_list(report.report), name_list[i]),
                             on='grid_number', how='inner')
    concat_df = concat_date_df(report, concat_df)  # concat date df

    insert_data(concat_df)

def make_df(grid_map, report, evt_cl_cd_mask_list, end_cd_mask_list, name_list):
    new_df = pd.DataFrame()
    for i in range(len(name_list)):
        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        count_point_df = count_point_in_polygon(grid_map,
                                                '격자고유번호',
                                                report.loc[evt_cl_cd_mask_list & end_cd_mask_list[i]],
                                                'x', 'y',
                                                EPSG_4326, False)

        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(lambda x: x[-6:])
    return new_df

def concat_date_df(report, new_df):
    new_df.insert(0, 'weekday', str(report.weekday.iloc[0]))
    new_df.insert(0, 'day_month_year', str(report.day.iloc[0]))
    new_df.insert(0, 'month', str(report.day.iloc[0])[4:6])
    new_df.insert(0, 'year', str(report.day.iloc[0])[0:4])
    return new_df


def insert_data(df):
    insert_list= []
    for idx, row in df.iterrows():
        insert_list.append(to_insert_list(row))

    from app.database.query.report import insert_report
    insert_report(insert_list)
