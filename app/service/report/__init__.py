from app.utils.codebook import *


def evt_cl_cd_mask_list(report):
    return [
        (report.evt_cl_cd == EVT_CL_CD_가정폭력),
        (report.evt_cl_cd == EVT_CL_CD_주거침입),
        (report.evt_cl_cd == EVT_CL_CD_성폭력),
        (report.evt_cl_cd == EVT_CL_CD_데이트폭력) | (report.evt_cl_cd == EVT_CL_CD_스토킹),
        (report.evt_cl_cd == EVT_CL_CD_데이트폭력),
        (report.evt_cl_cd == EVT_CL_CD_스토킹),
        (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내) | (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내),
        (report.evt_cl_cd == EVT_CL_CD_학교폭력),
    ]


name_list = [
    ["dv_arrest", "dv_investigation", "dv_end_report", "dv_not_handle"],
    ["tp_arrest", "tp_investigation", "tp_end_report", "tp_not_handle"],
    ["sh_arrest", "sh_investigation", "sh_end_report", "sh_not_handle"],
    ["ds_arrest", "ds_investigation", "ds_end_report", "ds_not_handle"],
    ["da_arrest", "da_investigation", "da_end_report", "da_not_handle"],
    ["st_arrest", "st_investigation", "st_end_report", "st_not_handle"],
    ["ca_arrest", "ca_investigation", "ca_end_report", "ca_not_handle"],
    ["sv_arrest", "sv_investigation", "sv_end_report", "sv_not_handle"],

]


def to_insert_list(df):
    return (df['year'], df['month'], df['day_month_year'], df['weekday'], df['grid_number'],
            df['dv_arrest'], df['dv_investigation'], df['dv_end_report'], df['dv_not_handle'],
            df['tp_arrest'], df['tp_investigation'], df['tp_end_report'], df['tp_not_handle'],
            df['sh_arrest'], df['sh_investigation'], df['sh_end_report'], df['sh_not_handle'],
            df['ds_arrest'], df['ds_investigation'], df['ds_end_report'], df['ds_not_handle'],
            df['da_arrest'], df['da_investigation'], df['da_end_report'], df['da_not_handle'],
            df['st_arrest'], df['st_investigation'], df['st_end_report'], df['st_not_handle'],
            df['ca_arrest'], df['ca_investigation'], df['ca_end_report'], df['ca_not_handle'],
            df['sv_arrest'], df['sv_investigation'], df['sv_end_report'], df['sv_not_handle'])