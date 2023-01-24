from pandas import DataFrame

from app.business.preprocessing.utils.utils import get_weekday
from app.database.query.report import insert_report
from app.utils.codebook import *
from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
import pandas as pd

from app.utils.constants import *
from app.utils.utils import slice_grid_number

'''
@Param
grid_map : 격자 데이터를 의미함
report_df : 112 신고건수 데이터를 의미함
'''
def service(grid_map, report_df):
    #데이터를 필터링 하기위한 4개의 종결코드 카테고리에 대한 종결코드 마스크 리스트를 만듬  (검거,계속조사,신고종결,미처리)
    end_cd_mask_list = [end_cd_arrest_mask(report_df), end_cd_investigation_mask(report_df),
                        end_cd_end_report_mask(report_df), end_cd_not_handle_mask(report_df)]
    # 산출 데이터 프레임을 만듦
    concat_df = DataFrame()
    # 격자 고유번호의 앞자리 ("다사")를 제거함
    concat_df['grid_number'] = grid_map['격자고유번호'].map(slice_grid_number)

    # 사건종별코드 (총 8개) 별로 4종의 종결 코드 건수를 산출하기위한 코드입니다. 전부 로직은 동일, 리팩토링 얘정
    # 가정폭력,주거침입,성폭력,데이트폭력-스토킹,데이트폭력,스토킹,아동학대,학교폭력
    # 각각 카테고리별로 df를 만들어내고  df 8개를 합침
    concat_df = pd.merge(concat_df, make_dv(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_tp(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_sh(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ds(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_da(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_st(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_ca(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')
    concat_df = pd.merge(concat_df, make_sv(grid_map, report_df, end_cd_mask_list), on='grid_number',
                         how='inner')

    # 부가적인 컬럼들 (년월일 등) 추가하여 합침
    concat_df = concat_sub_data(report_df, concat_df)


    # 최종적으로 DB에 삽입함
    insert_data(concat_df)


def make_dv(grid_map, report_df, end_cd_mask_list):
    # 사건 종별 코드중 가정폭력에 해당하는 것만 모음
    dv_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_가정폭력)
    # 4개의 컬럼을 사전에 만들어둠
    name_list = ["dv_arrest", "dv_investigation", "dv_end_report", "dv_not_handle"]
    new_df = DataFrame()

    for i in range(4):
        # 가정폭력과 4개의 종결코드 마스크에 대하여 필터링된 데이터를 저장함
        temp_df = report_df.loc[dv_evt_cl_mask & end_cd_mask_list[i]] # 종결코드 및 가정폭력 필터링
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False) # 필터링 된 데이터를 바탕으로 격자내 포함하는 신고건수들을 산출해냄 (return df[['count']['격자번호']])
        # 산출된 데이터와 기존 데이터랑 데이터 위치 맞추기 위해서 하는 작업
        # 지하철 관광지 한강 경찰대에 경우에는 지역별 격자 데이터로 merge 한다
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')

        # 격자와 count를 가지고 있는 df를 반환함
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_tp(grid_map, report_df, end_cd_mask_list):
    tp_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_주거침입)
    name_list = ["tp_arrest", "tp_investigation", "tp_end_report", "tp_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[tp_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_sh(grid_map, report_df, end_cd_mask_list):
    sh_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_성폭력)
    name_list = ["sh_arrest", "sh_investigation", "sh_end_report", "sh_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[sh_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_ds(grid_map, report_df, end_cd_mask_list):
    ds_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_데이트폭력) | (report_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["ds_arrest", "ds_investigation", "ds_end_report", "ds_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[ds_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_da(grid_map, report_df, end_cd_mask_list):
    da_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_데이트폭력)
    name_list = ["da_arrest", "da_investigation", "da_end_report", "da_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[da_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_st(grid_map, report_df, end_cd_mask_list):
    st_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_스토킹)
    name_list = ["st_arrest", "st_investigation", "st_end_report", "st_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[st_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_ca(grid_map, report_df, end_cd_mask_list):
    ca_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_아동학대_가정내) | (report_df.EVT_CL_CD == EVT_CL_CD_아동학대_가정내)

    name_list = ["ca_arrest", "ca_investigation", "ca_end_report", "ca_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[ca_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)

    return new_df


def make_sv(grid_map, report_df, end_cd_mask_list):
    sv_evt_cl_mask = (report_df.EVT_CL_CD == EVT_CL_CD_학교폭력)
    name_list = ["sv_arrest", "sv_investigation", "sv_end_report", "sv_not_handle"]
    new_df = DataFrame()
    for i in range(4):
        temp_df = report_df.loc[sv_evt_cl_mask & end_cd_mask_list[i]]
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호', temp_df, 'x', 'y', EPSG_4326, False)
        concat_df = pd.merge(grid_map, count_point_df, on='격자고유번호', how='left')
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(slice_grid_number)
    return new_df


def concat_sub_data(report_df, new_df):
    new_df['weekday']= get_weekday(str(report_df['DAY'].iloc[0]))
    new_df['day_month_year'] = str(report_df['DAY'].iloc[0])
    new_df['month']= str(report_df['DAY'].iloc[0])[4:6]
    new_df['year']= str(report_df['DAY'].iloc[0])[0:4]
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
