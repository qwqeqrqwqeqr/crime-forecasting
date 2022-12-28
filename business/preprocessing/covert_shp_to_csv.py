

import geopandas as gpd


def read_shp(path,encoding):
    return gpd.read_file(path, encoding = encoding)


def convert_csv(inputpath,outputpath,encoding):
    df = read_shp(inputpath,encoding)


    print(df['geometry'])
    print(type(df['geometry']))
