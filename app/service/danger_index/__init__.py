
from app.utils.codebook import *


def to_insert_list(df):
    return (
    df['grid_number'], df['dv_danger_index'], df['tp_danger_index'],
    df['sh_danger_index'], df['da_danger_index'],
    df['st_danger_index'], df['ca_danger_index'], df['sv_danger_index'])



def evt_cl_cd_mask_list(report):        # 가정 폭력 / 주거 침입 / 성폭력 / 데이트폭력 / 스토킹 / 아동학대 / 학교폭력
    return [
        (report.evt_cl_cd == EVT_CL_CD_가정폭력),
        (report.evt_cl_cd == EVT_CL_CD_주거침입),
        (report.evt_cl_cd == EVT_CL_CD_성폭력),
        (report.evt_cl_cd == EVT_CL_CD_데이트폭력),
        (report.evt_cl_cd == EVT_CL_CD_스토킹),
        (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내) | (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내),
        (report.evt_cl_cd == EVT_CL_CD_학교폭력)
    ]



DANGER_INDEX_NAME_LIST = ["dv_danger_index", "tp_danger_index", "sh_danger_index", "da_danger_index", "st_danger_index",
             "ca_danger_index", "sv_danger_index"]


from datetime import date
from app.utils.constants import PATH_DANGER_INDEX_DATA
DANGER_INDEX_DATA_PATH = lambda key_danger_index: PATH_DANGER_INDEX_DATA + str(date.today()) + "_" + key_danger_index.replace('_', '-') + ".csv"