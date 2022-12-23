import geopandas as gpd
from util.constants import *


def count_point_in_polygon():

    grid_geojson = gpd.read_file(PATH_격자_MAP, driver="GeoJSON")

    print(grid_geojson)