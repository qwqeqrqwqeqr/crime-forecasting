import sys

import pandas as pd
import geopandas as gpd

from app.business.preprocessing.utils.utils import get_center_coordinate
from app.utils.constants import *

'''
입력 신고 데이터 포멧 : KPU_99_YYYYMMDD_C_001.csv 
argv[1] : 112 신고 데이터
EVT_CL_CD : 사건 종별 코드를 의미함
END_CD : 종결 코드를 의미
PATH_GRID_HANGANG_MAP : 한강 격자 데이터
PATH_GRID_MAP : 격자 데이터
'''

CRIME_REPORT_PATH = sys.argv[1]


if __name__ == '__main__':
    from app.utils.utils import init
    init()          # 초기 검사

    print("========== 112신고 빈도데이터 - [한강 경찰대]를 산출 합니다. ==========")

    area_map = pd.read_csv(PATH_GRID_HANGANG_MAP, encoding=UTF_8)

    from app.model.report import Report
    report = Report(pd.read_csv(CRIME_REPORT_PATH, encoding=UTF_8))

    from app.model.grid_map import GridMap
    grid_map = GridMap(PATH_GRID_MAP)

    for day_month_year in report.get_day_list():
        from app.service.hangang.service import service
        service(area_map,grid_map,report.get_report_filtered_day(day_month_year))


