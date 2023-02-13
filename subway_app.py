# -*- coding: utf-8 -*-

from app.utils.constants import *

'''
Run Parameters
- REPORT_PATH: report file path (ex) "./test/data/report/POL_01_20220101.csv"

PATH_GRID_MAP : 100 grid data 
PATH_GRID_SUBWAY_MAP : subway grid data
'''

import sys

REPORT_PATH = sys.argv[1]

import warnings

warnings.filterwarnings(action='ignore')

if __name__ == '__main__':

    from app.business.validator.validate_file import check_data

    check_data()  # Check directory & data file

    import pandas as pd

    grid_subway_map = pd.read_csv(PATH_GRID_SUBWAY_MAP, encoding=UTF_8)

    from app.business.validator.validate_dataframe import validate_subway_grid_df

    validate_subway_grid_df(grid_subway_map)
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

        logger.info(f"[지하철 경찰대] [%s] 데이터를 산출합니다" %day_month_year)
        from app.service.subway.service import service

        service(grid_subway_map, grid_map, report.get_report_filtered_day(day_month_year))
