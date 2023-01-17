from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.hangang import insert_hangang
from app.database.query.subway import insert_subway
from app.utils.code_book import *
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
    concat_df = pd.merge(concat_df, make_pp(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_gc(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_cr(area_map, grid_map, origin_df, end_cd_mask_list), on='grid_number',
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
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, "./test.csv", 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_pp(area_map, grid_map, origin_df, end_cd_mask_list):
    pp_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_분실습득) | (origin_df.EVT_CL_CD == EVT_CL_CD_절도) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_재물손괴) |  (origin_df.EVT_CL_CD == EVT_CL_CD_사기)
    name_list = ["pp_arrest", "pp_investigation", "pp_end_report", "pp_not_handle"]
    new_df = DataFrame()

    for i in range(4):
        temp_df = origin_df.loc[pp_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, "./test.csv", 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_gc(area_map, grid_map, origin_df, end_cd_mask_list):
    gc_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_성폭력) | (origin_df.EVT_CL_CD == EVT_CL_CD_데이트폭력) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["gc_arrest", "gc_investigation", "gc_end_report", "gc_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[gc_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, "./test.csv", 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호']

    return new_df


def make_cr(area_map, grid_map, origin_df, end_cd_mask_list):
    cr_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_시비) | (origin_df.EVT_CL_CD == EVT_CL_CD_폭력) | (
            origin_df.EVT_CL_CD == EVT_CL_CD_행패소란) | (origin_df.EVT_CL_CD == EVT_CL_CD_주취자)
    name_list = ["cr_arrest", "cr_investigation", "cr_end_report", "cr_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[cr_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, "./test.csv", 'x', 'y', EPSG_4326, False)
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
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, "./test.csv", 'x', 'y', EPSG_4326, False)
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
         row['pp_arrest'], row['pp_investigation'], row['pp_end_report'], row['pp_not_handle'],
         row['gc_arrest'], row['gc_investigation'], row['gc_end_report'], row['gc_not_handle'],
         row['cr_arrest'], row['cr_investigation'], row['cr_end_report'], row['cr_not_handle'],
         row['md_arrest'], row['md_investigation'], row['md_end_report'], row['md_not_handle']))
    insert_subway(temp_list)
