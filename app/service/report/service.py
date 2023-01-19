from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.report import insert_report
from app.utils.code import *
from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
import pandas as pd

from app.utils.constants import *
from app.utils.utils import slice_grid_number


def service(grid_map, origin_df):
    end_cd_mask_list = [end_cd_arrest_mask(origin_df), end_cd_investigation_mask(origin_df),
                        end_cd_end_report_mask(origin_df), end_cd_not_handle_mask(origin_df)]
    concat_df = DataFrame()
    concat_df['grid_number'] = grid_map['격자고유번호'].map(slice_grid_number)

    concat_df = pd.merge(concat_df, make_dv(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_tp(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_sh(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ds(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_da(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_st(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ca(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_sv(grid_map, origin_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = concat_sub_data(origin_df, concat_df)

    insert_data(concat_df)


def make_dv(grid_map, origin_df, end_cd_mask_list):
    dv_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_가정폭력)
    name_list = ["dv_arrest", "dv_investigation", "dv_end_report", "dv_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[dv_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_tp(grid_map, origin_df, end_cd_mask_list):
    tp_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_주거침입)
    name_list = ["tp_arrest", "tp_investigation", "tp_end_report", "tp_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[tp_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_sh(grid_map, origin_df, end_cd_mask_list):
    sh_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_성폭력)
    name_list = ["sh_arrest", "sh_investigation", "sh_end_report", "sh_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[sh_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_ds(grid_map, origin_df, end_cd_mask_list):
    ds_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_데이트폭력) | (origin_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["ds_arrest", "ds_investigation", "ds_end_report", "ds_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[ds_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_da(grid_map, origin_df, end_cd_mask_list):
    da_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_데이트폭력)
    name_list = ["da_arrest", "da_investigation", "da_end_report", "da_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[da_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_st(grid_map, origin_df, end_cd_mask_list):
    st_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["st_arrest", "st_investigation", "st_end_report", "st_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[st_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_ca(grid_map, origin_df, end_cd_mask_list):
    ca_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_아동학대_가정내) | (origin_df.EVT_CL_CD == EVT_CL_CD_아동학대_가정내)

    name_list = ["ca_arrest", "ca_investigation", "ca_end_report", "ca_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[ca_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_sv(grid_map, origin_df, end_cd_mask_list):
    sv_evt_cl_mask = (origin_df.EVT_CL_CD == EVT_CL_CD_학교폭력)
    name_list = ["sv_arrest", "sv_investigation", "sv_end_report", "sv_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = origin_df.loc[sv_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
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
                          row['dv_arrest'], row['dv_investigation'], row['dv_end_report'], row['dv_not_handle'],
                          row['tp_arrest'], row['tp_investigation'], row['tp_end_report'], row['tp_not_handle'],
                          row['sh_arrest'], row['sh_investigation'], row['sh_end_report'], row['sh_not_handle'],
                          row['ds_arrest'], row['ds_investigation'], row['ds_end_report'], row['ds_not_handle'],
                          row['da_arrest'], row['da_investigation'], row['da_end_report'], row['da_not_handle'],
                          row['st_arrest'], row['st_investigation'], row['st_end_report'], row['st_not_handle'],
                          row['ca_arrest'], row['ca_investigation'], row['ca_end_report'], row['ca_not_handle'],
                          row['sv_arrest'], row['sv_investigation'], row['sv_end_report'], row['sv_not_handle']))
        insert_report(temp_list)
