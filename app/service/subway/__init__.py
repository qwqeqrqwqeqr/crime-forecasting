from app.utils.codebook import *


def evt_cl_cd_mask_list(report):        # 사고 예방 / 재산 보호 / 젠더 보호 / 범죄 신고 / 대형 사건
    return  [
    (report.evt_cl_cd == EVT_CL_CD_보호조치) | (report.evt_cl_cd == EVT_CL_CD_위험방지) | (
            report.evt_cl_cd == EVT_CL_CD_비상벨),
    (report.evt_cl_cd == EVT_CL_CD_분실습득) | (report.evt_cl_cd == EVT_CL_CD_절도) | (
            report.evt_cl_cd == EVT_CL_CD_재물손괴) | (report.evt_cl_cd == EVT_CL_CD_사기),
    (report.evt_cl_cd == EVT_CL_CD_성폭력) | (report.evt_cl_cd == EVT_CL_CD_데이트폭력) | (
            report.evt_cl_cd == EVT_CL_CD_스토킹),
    (report.evt_cl_cd == EVT_CL_CD_시비) | (report.evt_cl_cd == EVT_CL_CD_폭력) | (
            report.evt_cl_cd == EVT_CL_CD_행패소란) | (report.evt_cl_cd == EVT_CL_CD_주취자),
    ((report.evt_cl_cd == EVT_CL_CD_화재) | (report.evt_cl_cd == EVT_CL_CD_재해재난)) & (
            report.RECV_EMG_CD == RECV_EMG_CD_긴급)]

name_list = [
    ["ac_arrest", "ac_investigation", "ac_end_report", "ac_not_handle"],
    ["pp_arrest", "pp_investigation", "pp_end_report", "pp_not_handle"],
    ["gc_arrest", "gc_investigation", "gc_end_report", "gc_not_handle"],
    ["cr_arrest", "cr_investigation", "cr_end_report", "cr_not_handle"],
    ["md_arrest", "md_investigation", "md_end_report", "md_not_handle"]
]

def to_insert_list(df):
    return (df['year'], df['month'], df['day_month_year'], df['weekday'], df['grid_number'],
     df['ac_arrest'], df['ac_investigation'], df['ac_end_report'], df['ac_not_handle'],
     df['pp_arrest'], df['pp_investigation'], df['pp_end_report'], df['pp_not_handle'],
     df['gc_arrest'], df['gc_investigation'], df['gc_end_report'], df['gc_not_handle'],
     df['cr_arrest'], df['cr_investigation'], df['cr_end_report'], df['cr_not_handle'],
     df['md_arrest'], df['md_investigation'], df['md_end_report'], df['md_not_handle'],
     df['name'])