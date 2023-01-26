from app.utils.codebook import *


def evt_cl_cd_mask_list(report):
    return [
        (report.evt_cl_cd == EVT_CL_CD_보호조치) | (report.evt_cl_cd == EVT_CL_CD_위험방지) | (
                report.evt_cl_cd == EVT_CL_CD_비상벨),
        (report.evt_cl_cd == EVT_CL_CD_자살) | (report.evt_cl_cd == EVT_CL_CD_구조요청) | (
                report.evt_cl_cd == EVT_CL_CD_변사자),
        (report.evt_cl_cd == EVT_CL_CD_교통사고) | (report.evt_cl_cd == EVT_CL_CD_교통불편) | (
                report.evt_cl_cd == EVT_CL_CD_교통위반) | (report.evt_cl_cd == EVT_CL_CD_음주운전) | (
                report.evt_cl_cd == EVT_CL_CD_사망_대형사고),
        ((report.evt_cl_cd == EVT_CL_CD_화재) | (report.evt_cl_cd == EVT_CL_CD_재해재난)) & (
                report.RECV_EMG_CD == RECV_EMG_CD_긴급)
    ]


name_list = [
    ["ac_arrest", "ac_investigation", "ac_end_report", "ac_not_handle"],
    ["ls_arrest", "ls_investigation", "ls_end_report", "ls_not_handle"],
    ["ts_arrest", "ts_investigation", "ts_end_report", "ts_not_handle"],
    ["md_arrest", "md_investigation", "md_end_report", "md_not_handle"],

]


def to_insert_list(df):
    return (df['year'], df['month'], df['day_month_year'], df['weekday'], df['grid_number'],
            df['ac_arrest'], df['ac_investigation'], df['ac_end_report'], df['ac_not_handle'],
            df['ls_arrest'], df['ls_investigation'], df['ls_end_report'], df['ls_not_handle'],
            df['ts_arrest'], df['ts_investigation'], df['ts_end_report'], df['ts_not_handle'],
            df['md_arrest'], df['md_investigation'], df['md_end_report'], df['md_not_handle'], df['name_x'].iloc[1])
