
import pandas as pd


from app.utils.constants import *

'''
Run Parameters
- REPORT_PATH: report directory path (ex) "./test/data/report/"
- LIFE_POPULATION_PATH: life population directory path (ex) "./test/data/life_population/"

PATH_GRID_MAP : 100 grid data 
PATH_GRID_AREA_MAP : area(집계구) grid data
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

    from app.model.grid_map import GridMap
    import geopandas as gpd

    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")
    from app.business.validator.validate_dataframe import validate_grid_df

    validate_grid_df(grid_map)  # validate grid
    grid_map = GridMap(grid_map)  # 100 grid data dataframe

    grid_area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)
    from app.business.validator.validate_dataframe import validate_area_grid_df

    validate_area_grid_df(grid_area_map)

    temp_life_population = []
    for item in os.listdir(LIFE_POPULATION_DIRECTORY_PATH):
        life_population_item = pd.read_csv(LIFE_POPULATION_DIRECTORY_PATH + item, encoding=EUC_KR)
        from app.business.validator.validate_dataframe import validate_life_population_df
        validate_life_population_df(life_population_item)  # validate life population dataframe
        temp_life_population.append(life_population_item)

    temp_report = []
    for item in os.listdir(REPORT_DIRECTORY_PATH):
        report_item = pd.read_csv(REPORT_DIRECTORY_PATH + item, encoding=UTF_8)
        from app.business.validator.validate_dataframe import validate_report_df
        validate_report_df(report_item)  # validate report dataframe
        temp_report.append(report_item)

    from log import logger
    logger.info(f"[위험지수] 데이터를 산출합니다")

    from app.model.life_population import LifePopulation
    from app.model.report import Report
    from app.service.danger_index.service import service
    service(LifePopulation(pd.concat(temp_life_population)),Report(pd.concat(temp_report)),grid_map,grid_area_map)

