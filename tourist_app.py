# -*- coding: utf-8 -*-

from app.utils.constants import *

'''
Run Parameters
- REPORT_PATH: report file path (ex) "./test/data/report/POL_01_20220101_M.csv"

PATH_GRID_MAP : 100 grid data 
PATH_GRID_TOURIST_MAP : tourist grid data
'''

import sys

REPORT_PATH = sys.argv[1]

import warnings

warnings.filterwarnings(action='ignore')

if __name__ == '__main__':

    from app.business.validator.validate_file import init, check_file

    init()  # Check directory & data file
    check_file(REPORT_PATH)  # Check Report file

    import pandas as pd

    grid_tourist_map = pd.read_csv(PATH_GRID_TOURIST_MAP, encoding=UTF_8)  # tourist grid data

    from app.business.validator.validate_dataframe import validate_tourist_grid_df

    validate_tourist_grid_df(grid_tourist_map)
    from app.model.report import Report

    import pandas as pd

    report = pd.read_csv(REPORT_PATH, encoding=UTF_8)
    from app.business.validator.validate_dataframe import validate_report_df

    validate_report_df(report)  # validate report dataframe
    report = Report(report)  # report data

    from app.model.grid_map import GridMap
    import geopandas as gpd

    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")
    from app.business.validator.validate_dataframe import validate_grid_df

    validate_grid_df(grid_map)  # validate grid

    grid_map = GridMap(grid_map)  # 100 grid data dataframe

    for day_month_year in report.get_day_list():
        from log import logger

        logger.info(f"[관광지 경찰대] [%s] 데이터를 산출합니다" % day_month_year)
        from app.service.tourist.service import service

        service(grid_tourist_map, grid_map, report.get_report_filtered_day(day_month_year))
