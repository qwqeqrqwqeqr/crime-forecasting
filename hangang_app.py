# -*- coding: utf-8 -*-

import pandas as pd
from log import logger

from app.utils.constants import *

'''
112 신고 데이터 형식 : POL_01_YYYYMMDD_M.csv 
CRIME_REPORT_PATH : 112 신고 데이터
PATH_GRID_HANGANG_MAP : 한강 격자 데이터
PATH_GRID_MAP : 격자 데이터
'''

import sys
CRIME_REPORT_PATH = sys.argv[1]


if __name__ == '__main__':

    import warnings
    warnings.filterwarnings(action='ignore')

    from app.utils.utils import init
    init()          # 초기 검사

    print("========== 112신고 빈도데이터 - [한강 경찰대]를 산출 합니다. ==========")

    grid_hangang_map = pd.read_csv(PATH_GRID_HANGANG_MAP, encoding=UTF_8)

    from app.model.report import Report
    report = Report(pd.read_csv(CRIME_REPORT_PATH, encoding=UTF_8))

    from app.model.grid_map import GridMap
    grid_map = GridMap(PATH_GRID_MAP)




    for day_month_year in report.get_day_list():

        logger.info(f"[한강 경찰대] [%s] 데이터를 산출합니다" % day_month_year)
        from app.service.hangang.service import service
        service(grid_hangang_map,grid_map,report.get_report_filtered_day(day_month_year))


