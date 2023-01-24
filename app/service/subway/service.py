from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.subway import insert_subway
from app.service.subway.constants import evt_cl_cd_mask_list, name_list
from app.utils.codebook import *
from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
import pandas as pd

from app.utils.constants import *
from app.utils.utils import slice_grid_number


def service(area_map, grid_map, report):


    concat_df = DataFrame()
    concat_df['grid_number'] = area_map['격자고유번호'].map(slice_grid_number)

    for i in range(len(name_list)):
        concat_df = pd.merge(concat_df,
                             make_df(area_map,grid_map,report,evt_cl_cd_mask_list(report)[i],end_cd_mask_list(report),name_list[i]),
                             on='grid_number',how='inner')

    concat_df = concat_sub_data(report, concat_df)

    insert_data(concat_df)


def make_df(area_map,grid_map,report,evt_cl_cd_mask_list,end_cd_mask_list,name_list):
    new_df = DataFrame()
    for i in range(len(name_list)):
        temp_df = report.loc[evt_cl_cd_mask_list & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['지하철']
    return new_df




def concat_sub_data(report, new_df):
    new_df.insert(0, 'weekday', get_weekday(str(report['DAY'].iloc[0])))
    new_df.insert(0, 'day_month_year', str(report['DAY'].iloc[0]))
    new_df.insert(0, 'month', str(report['DAY'].iloc[0])[4:6])
    new_df.insert(0, 'year', str(report['DAY'].iloc[0])[0:4])
    return new_df


def insert_data(df):
    temp_list = []
    for idx, row in df.iterrows():
        temp_list.append((row['year'], row['month'], row['day_month_year'], row['weekday'], row['grid_number'],
                          row['ac_arrest'], row['ac_investigation'], row['ac_end_report'], row['ac_not_handle'],
                          row['pp_arrest'], row['pp_investigation'], row['pp_end_report'], row['pp_not_handle'],
                          row['gc_arrest'], row['gc_investigation'], row['gc_end_report'], row['gc_not_handle'],
                          row['cr_arrest'], row['cr_investigation'], row['cr_end_report'], row['cr_not_handle'],
                          row['md_arrest'], row['md_investigation'], row['md_end_report'], row['md_not_handle'],row['name']))
    insert_subway(temp_list)

