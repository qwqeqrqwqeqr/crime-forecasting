from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.tourist import insert_tourist
from app.utils.codebook import *
from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
import pandas as pd

from app.utils.constants import *
from app.utils.utils import slice_grid_number


def service(area_map, grid_map, report_df):
    end_cd_mask_list = [end_cd_arrest_mask(report_df), end_cd_investigation_mask(report_df),
                        end_cd_end_report_mask(report_df), end_cd_not_handle_mask(report_df)]
    concat_df = DataFrame()
    concat_df['grid_number'] = area_map['격자고유번호'].map(slice_grid_number)

    concat_df = pd.merge(concat_df, make_ac(area_map, grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_pp(area_map, grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_gc(area_map, grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ts(area_map, grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_md(area_map, grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = concat_sub_data(report_df, concat_df)

    insert_data(concat_df)


def make_ac(area_map, grid_map, report_df, end_cd_mask_list):
    ac_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_보호조치) | (report_df.EVT_CL_CD == EVT_CL_CD_위험방지) | (
            report_df.EVT_CL_CD == EVT_CL_CD_비상벨)
    name_list = ["ac_arrest", "ac_investigation", "ac_end_report", "ac_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[ac_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['관광지']
    return new_df


def make_pp(area_map, grid_map, report_df, end_cd_mask_list):
    pp_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_분실습득) | (report_df.EVT_CL_CD == EVT_CL_CD_절도) | (
            report_df.EVT_CL_CD == EVT_CL_CD_재물손괴) |  (report_df.EVT_CL_CD == EVT_CL_CD_사기)
    name_list = ["pp_arrest", "pp_investigation", "pp_end_report", "pp_not_handle"]
    new_df = DataFrame()

    for i in range(4):
        temp_df = report_df.loc[pp_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['관광지']
    return new_df


def make_gc(area_map, grid_map, report_df, end_cd_mask_list):
    gc_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_성폭력) | (report_df.EVT_CL_CD == EVT_CL_CD_데이트폭력) | (
            report_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["gc_arrest", "gc_investigation", "gc_end_report", "gc_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[gc_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['관광지']
    return new_df


def make_ts(area_map, grid_map, report_df, end_cd_mask_list):
    ts_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_교통사고) | (report_df.EVT_CL_CD == EVT_CL_CD_교통불편) | (
            report_df.EVT_CL_CD == EVT_CL_CD_교통위반) | (report_df.EVT_CL_CD == EVT_CL_CD_음주운전) | (report_df.EVT_CL_CD == EVT_CL_CD_사망_대형사고)
    name_list = ["ts_arrest", "ts_investigation", "ts_end_report", "ts_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[ts_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['관광지']
    return new_df


def make_md(area_map, grid_map, report_df, end_cd_mask_list):
    md_evt_cl_mask = ((report_df.EVT_CL_CD == EVT_CL_CD_화재) | (report_df.EVT_CL_CD == EVT_CL_CD_재해재난)) & (
            report_df.RECV_EMG_CD == RECV_EMG_CD_긴급)
    name_list = ["md_arrest", "md_investigation", "md_end_report", "md_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[md_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df,  'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
        new_df['name'] = concat_df['관광지']
    return new_df


def concat_sub_data(report_df, new_df):
    new_df.insert(0, 'weekday', get_weekday(str(report_df['DAY'].iloc[0])))
    new_df.insert(0, 'day_month_year', str(report_df['DAY'].iloc[0]))
    new_df.insert(0, 'month', str(report_df['DAY'].iloc[0])[4:6])
    new_df.insert(0, 'year', str(report_df['DAY'].iloc[0])[0:4])
    return new_df


def insert_data(df):
    temp_list = []
    for idx, row in df.iterrows():
        temp_list.append((row['year'], row['month'], row['day_month_year'], row['weekday'], row['grid_number'],
         row['ac_arrest'], row['ac_investigation'], row['ac_end_report'],row['ac_not_handle'],
         row['pp_arrest'], row['pp_investigation'], row['pp_end_report'], row['pp_not_handle'],
         row['gc_arrest'], row['gc_investigation'], row['gc_end_report'], row['gc_not_handle'],
         row['ts_arrest'], row['ts_investigation'], row['ts_end_report'], row['ts_not_handle'],
         row['md_arrest'], row['md_investigation'], row['md_end_report'], row['md_not_handle'],row['name']))
    insert_tourist(temp_list)
