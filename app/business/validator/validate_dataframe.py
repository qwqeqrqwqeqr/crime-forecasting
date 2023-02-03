from pandas import DataFrame
from app.business.validator import *


def validate_report_df(report: DataFrame):
    if False in report.columns.values == report_column_list:
        from log import logger
        logger.info("[Error] [Report] Incorrect file format")
        raise EnvironmentError


def validate_life_population_df(life_population: DataFrame):
    if False in life_population.columns.values == life_population_column_list:
        from log import logger
        logger.info("[Error] [Life Population] Incorrect file format")
        raise EnvironmentError


def validate_grid_df(grid: DataFrame):
    if False in grid.columns.values == grid_column_list:
        from log import logger
        logger.info("[Error] [Grid] Incorrect file format")
        raise EnvironmentError


def validate_tourist_grid_df(grid: DataFrame):
    if False in grid.columns.values == tourist_grid_column_list:
        from log import logger
        logger.info("[Error] [Tourist Grid] Incorrect file format")
        raise EnvironmentError

def validate_hangang_grid_df(grid: DataFrame):
    if False in grid.columns.values == hangang_grid_column_list:
        from log import logger
        logger.info("[Error] [Hangang Grid] Incorrect file format")
        raise EnvironmentError


def validate_subway_grid_df(grid: DataFrame):
    if False in grid.columns.values == subway_grid_column_list:
        from log import logger
        logger.info("[Error] [Subway Grid] Incorrect file format")
        raise EnvironmentError


def validate_congestion_grid_df(grid: DataFrame):
    if False in grid.columns.values == congestion_grid_column_list:
        from log import logger
        logger.info("[Error] [Congestion Grid] Incorrect file format")
        raise EnvironmentError

def validate_area_grid_df(grid: DataFrame):
    if False in grid.columns.values == area_grid_column_list:
        from log import logger
        logger.info("[Error] [Area Grid] Incorrect file format")
        raise EnvironmentError