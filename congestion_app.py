# -*- coding: utf-8 -*-

import pandas as pd

from app.utils.constants import *
from log import logger


'''
혼잡도는 1달 단위로 계산함
CRIME_REPORT_PATH :  폴더로 지정
LIFE_POPULATION_PATH :  폴더로 지정
PATH_GRID_AREA_MAP : 집계구 격자 데이터
PATH_GRID_CONGESTION_MAP : 혼잡 지역(실시간 도시) 데이터
PATH_GRID_MAP : 격자 데이터
'''

import os
import sys

CRIME_REPORT_PATH = sys.argv[1]
LIFE_POPULATION_PATH = sys.argv[2]

if __name__ == '__main__':

    import warnings

    warnings.filterwarnings(action='ignore')

    from app.utils.utils import init

    init()  # 초기 검사

    temp_life_population = []
    for item in os.listdir(LIFE_POPULATION_PATH):
        temp_life_population.append(pd.read_csv(LIFE_POPULATION_PATH + item, encoding=EUC_KR))

    from app.model.life_population import LifePopulation

    life_population = LifePopulation(pd.concat(temp_life_population))  # 생활인구 통합

    temp_report = []
    for item in os.listdir(CRIME_REPORT_PATH):
        temp_report.append(pd.read_csv(CRIME_REPORT_PATH + item, encoding=UTF_8))

    from app.model.report import Report

    report = Report(pd.concat(temp_report))  # 112 신고 건수 통합

    from app.model.grid_map import GridMap

    grid_map = GridMap(PATH_GRID_MAP)  # 100격자

    grid_area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)
    grid_congestion_map = pd.read_csv(PATH_GRID_CONGESTION_MAP, encoding=UTF_8)


    for day_month_year in life_population.get_day_list():
        logger.info(f"[혼잡도] [%s] 데이터를 산출합니다" % day_month_year)

        from app.service.congestion.service import service

        service(grid_area_map, grid_congestion_map, grid_map,
                life_population.get_life_population_filtered_day(day_month_year),
                report.get_report_filtered_day(day_month_year))
