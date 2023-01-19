from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.hangang import insert_hangang
from app.utils.code import *
from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
import pandas as pd

from app.utils.constants import *


def service(area_map, grid_map, origin_df):
    end_cd_mask_list = [end_cd_arrest_mask(origin_df), end_cd_investigation_mask(origin_df),
                        end_cd_end_report_mask(origin_df), end_cd_not_handle_mask(origin_df)]
    concat_df = DataFrame()
    concat_df['grid_number'] = area_map['격자고유번호']

    concat_df = pd.merge(concat_df, make_ac(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ls(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ts(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_md(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = concat_sub_data(origin_df, concat_df)

    insert_data(concat_df)


def make_ac(area_map, grid_map, origin_df, end_cd_mask_list):
    ac_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_보호조치) | (origin_df.EVT_CL_CD == EVT_CL_CD_위험방지) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_비상벨)
    name_list = ["ac_arrest", "ac_investigation", "ac_end_report", "ac_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[ac_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_ls(area_map, grid_map, origin_df, end_cd_mask_list):
    ls_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_자살) | (origin_df.EVT_CL_CD == EVT_CL_CD_구조요청) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_변사자)
    name_list = ["ls_arrest", "ls_investigation", "ls_end_report", "ls_not_handle"]
    new_df = DataFrame()

    for i in range(4):
        temp_df = origin_df.loc[ls_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_ts(area_map, grid_map, origin_df, end_cd_mask_list):
    ts_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_교통사고) | (origin_df.EVT_CL_CD == EVT_CL_CD_교통불편) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_교통위반) | (origin_df.EVT_CL_CD == EVT_CL_CD_음주운전) | (
                             origin_df.EVT_CL_CD == EVT_CL_CD_사망_대형사고)
    name_list = ["ts_arrest", "ts_investigation", "ts_end_report", "ts_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[ts_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_md(area_map, grid_map, origin_df, end_cd_mask_list):
    md_evt_cl_mask = ((origin_df.EVT_CL_CD == EVT_CL_CD_화재) | (origin_df.EVT_CL_CD == EVT_CL_CD_재해재난)) & (
            origin_df.RECV_EMG_CD == RECV_EMG_CD_긴급)
    name_list = ["md_arrest", "md_investigation", "md_end_report", "md_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[md_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def concat_sub_data(origin_df, new_df):
    new_df.insert(0, 'weekday', get_weekday(str(origin_df['DAY'].iloc[0])))
    new_df.insert(0, 'day_month_year', str(origin_df['DAY'].iloc[0]))
    new_df.insert(0, 'month', str(origin_df['DAY'].iloc[0])[4:6])
    new_df.insert(0, 'year', str(origin_df['DAY'].iloc[0])[0:4])
    return new_df


def insert_data(df):
    temp_list = []
    for idx, row in df.iterrows():
        temp_list.append((row['year'], row['month'], row['day_month_year'], row['weekday'], row['grid_number'],
         row['ac_arrest'], row['ac_investigation'], row['ac_end_report'],row['ac_not_handle'],
         row['ls_arrest'], row['ls_investigation'], row['ls_end_report'], row['ls_not_handle'],
         row['ts_arrest'], row['ts_investigation'], row['ts_end_report'], row['ts_not_handle'],
         row['md_arrest'], row['md_investigation'], row['md_end_report'], row['md_not_handle']))
    insert_hangang(temp_list)
