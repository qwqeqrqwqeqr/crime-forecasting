from app.utils.codebook import *

NAME_LIST = ["dv_danger_index", "tp_danger_index", "sh_danger_index", "da_danger_index", "st_danger_index",
             "ca_danger_index", "sv_danger_index"]

GRID_NAME_LIST = [
    '112신고데이터', '생활인구', 'CCTV', '보안등', '편의점', '여성안심지킴이집', '여성안심택배함', '아동안전지킴이시설물', '인터넷컴퓨터게임시설', '노래연습장', '단란주점',
    '유흥주점', '목욕장업', '숙박업', '지구대/파출소', '치안센터', '접수경찰서']

NAME_LIST_SIZE= len(NAME_LIST)
GRID_NAME_LIST_SIZE= len(GRID_NAME_LIST)

def evt_cl_cd_mask_list(report):
    return [
        (report.evt_cl_cd == EVT_CL_CD_가정폭력),
        (report.evt_cl_cd == EVT_CL_CD_주거침입),
        (report.evt_cl_cd == EVT_CL_CD_성폭력),
        (report.evt_cl_cd == EVT_CL_CD_데이트폭력),
        (report.evt_cl_cd == EVT_CL_CD_스토킹),
        (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내) | (report.evt_cl_cd == EVT_CL_CD_아동학대_가정내),
        (report.evt_cl_cd == EVT_CL_CD_학교폭력),
    ]



