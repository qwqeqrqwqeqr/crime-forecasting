# -*- coding: utf-8 -*-

import pandas as pd

from app.utils.constants import *

'''
Run Parameters
- REPORT_PATH: report directory path (ex) "./test/data/report/"
- LIFE_POPULATION_PATH: life population directory path (ex) "./test/data/life_population/"

 
PATH_AREA_CONGESTION_MAP
    - congestion(혼잡 지역,실시간 도시 데이터)와 집계구 정보를 가짐
    - 집계구의 공간 정보(geometry) 보유
'''

import os
import sys

REPORT_DIRECTORY_PATH = sys.argv[1]
LIFE_POPULATION_DIRECTORY_PATH = sys.argv[2]

import warnings

warnings.filterwarnings(action='ignore')

if __name__ == '__main__':

    from app.business.validator.validate_file import init
    init()  # Check directory & data file

    temp_life_population = []
    for item in os.listdir(LIFE_POPULATION_DIRECTORY_PATH): # loop in life population directory
        life_population_item = pd.read_csv(LIFE_POPULATION_DIRECTORY_PATH + item, encoding=EUC_KR)
        from app.business.validator.validate_dataframe import validate_life_population_df

        validate_life_population_df(life_population_item)  # validate life population dataframe
        temp_life_population.append(life_population_item)

    from app.model.life_population import LifePopulation
    life_population = LifePopulation(pd.concat(temp_life_population))  # concat life population df

    temp_report = []
    for item in os.listdir(REPORT_DIRECTORY_PATH): # loop in report directory
        report_item = pd.read_csv(REPORT_DIRECTORY_PATH + item, encoding=UTF_8)
        from app.business.validator.validate_dataframe import validate_report_df

        validate_report_df(report_item)  # validate report dataframe

        temp_report.append(report_item)

    from app.model.report import Report

    report = Report(pd.concat(temp_report))  # concat report df


    import geopandas as gpd
    area_congestion_map = gpd.read_file(PATH_AREA_CONGESTION_MAP, driver="GeoJSON")
    area_congestion_map = area_congestion_map.drop_duplicates('TOT_REG_CD')
    from app.business.validator.validate_dataframe import validate_congestion_area_df
    validate_congestion_area_df(area_congestion_map)


    for day_month_year in life_population.get_day_list():
        from log import logger
        logger.info(f"[혼잡도] [%s] 데이터를 산출합니다" % day_month_year)

        from app.service.congestion.service import service

        service(area_congestion_map,
                life_population.get_life_population_filtered_day(day_month_year),
                report.get_report_filtered_day(day_month_year))
