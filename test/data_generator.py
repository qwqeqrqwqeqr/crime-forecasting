import pandas as pd
import geopandas as gpd
from app.utils.constants import *

PATH_TEST_REPORT = "./test/data/report/POL_01_20220101_M.csv"
PATH_TEST_LIFE_POPULATION = "./test/data/life_population/LOCAL_PEOPLE_20220101.csv"

TEST_REPORT=pd.read_csv(PATH_TEST_REPORT, encoding=UTF_8)
TEST_LIFE_POPULATION=pd.read_csv(PATH_TEST_LIFE_POPULATION, encoding=EUC_KR)

TEST_GRID_MAP=gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")

TEST_GRID_HANGANG_MAP=pd.read_csv(PATH_GRID_HANGANG_MAP, encoding=UTF_8)
TEST_GRID_SUBWAY_MAP=pd.read_csv(PATH_GRID_SUBWAY_MAP, encoding=UTF_8)
TEST_GRID_TOURIST_MAP=pd.read_csv(PATH_GRID_TOURIST_MAP, encoding=UTF_8)

TEST_GRID_AREA_MAP=pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)
TEST_GRID_CONGESTION_MAP=pd.read_csv(PATH_GRID_CONGESTION_MAP, encoding=UTF_8)
TEST_AREA_CONGESTION_MAP=gpd.read_file(PATH_AREA_CONGESTION_MAP, driver="GeoJSON")
