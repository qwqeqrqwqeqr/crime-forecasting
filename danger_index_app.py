# -*- coding: utf-8 -*-

import pandas as pd


from app.utils.constants import *

'''
위험지수는 1달 단위로 계산함
CRIME_REPORT_PATH :  폴더로 지정
LIFE_POPULATION_PATH :  폴더로 지정
PATH_GRID_AREA_MAP : 집계구 격자 데이터
PATH_GRID_MAP : 격자 데이터
'''

import os
import sys

REPORT_PATH = sys.argv[1]
LIFE_POPULATION_PATH = sys.argv[2]

if __name__ == '__main__':

    import warnings

    warnings.filterwarnings(action='ignore')

    from app.business.validator.validate_file import init

    init()  # 초기 검사

    from app.model.grid_map import GridMap

    import geopandas as gpd

    grid_map = GridMap(gpd.read_file(PATH_GRID_MAP, driver="GeoJSON"))  # 100격자

    grid_area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)

    temp_life_population = []
    for item in os.listdir(LIFE_POPULATION_PATH):
        temp_life_population.append(pd.read_csv(LIFE_POPULATION_PATH + item, encoding=EUC_KR))


    temp_report = []
    for item in os.listdir(REPORT_PATH):
        temp_report.append(pd.read_csv(REPORT_PATH + item, encoding=UTF_8))

    from log import logger
    logger.info(f"[위험지수] [%s] 데이터를 산출합니다")

    from app.model.life_population import LifePopulation
    from app.model.report import Report
    from app.service.danger_index.service import service
    service(LifePopulation(pd.concat(temp_life_population)),Report(pd.concat(temp_report)),grid_map,grid_area_map)

