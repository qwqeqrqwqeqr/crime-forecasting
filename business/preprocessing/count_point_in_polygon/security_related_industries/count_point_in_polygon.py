import geopandas as gpd
import pandas as pd
import numpy as np
import pyproj
from geopandas import GeoDataFrame
from util.constants import *

'''
Param
count_point_in_polygon
    input_path => 데이터 입력경로
    output_path => 데이터 저장경로
    encoding => 인코딩 방식
    x_coordinate_name =>  x 좌표 이름
    y_coordinate_name =>  y 좌표 이름
    p1 => 현재 좌표계
    p2 => 타겟 좌표계

'''



def count_point_in_polygon(input_path,output_path,encoding,x_coordinate_name, y_coordinate_name,p1,p2):

    grid_geojson = gpd.read_file(PATH_격자_MAP, driver="GeoJSON")

    df = pd.read_csv(input_path, encoding=encoding)
    df['x'] = df[x_coordinate_name]
    df['y'] = df[y_coordinate_name]

    transform_coordinate_result = transform_coordinate(np.array(df[['x','y']]) , p1, p2)

    df['x'] = transform_coordinate_result[:,0]
    df['y'] = transform_coordinate_result[:,1]

    df = df[['x','y']]

    point = GeoDataFrame(df, geometry=gpd.points_from_xy(x=df.x, y=df.y),crs='epsg:4326')
    point.crs = grid_geojson.crs
    point_in_polygon = gpd.sjoin(point, grid_geojson[['격자고유번호', 'geometry']], how="inner", predicate='intersects')

    count_result = count_in_df(point_in_polygon)
    concat_result =  concat_df(count_result,grid_geojson)

    concat_result.to_csv(output_path,index=False)





def concat_df(subset_df,full_df):
    subset_df_grid_list = subset_df.격자고유번호.to_list()
    full_df_grid_list = full_df.격자고유번호.to_list()

    temp_df = pd.DataFrame({'격자고유번호': list(list(set(full_df_grid_list) - set(subset_df_grid_list)))})
    temp_df['count'] = 0

    crime_count_full = pd.concat([subset_df, temp_df])

    return crime_count_full[['격자고유번호','count']]


def count_in_df(df):
    df['count'] = 1
    return df.groupby(['격자고유번호']).sum().reset_index()

def transform_coordinate(coord, p1_type, p2_type):
    p1 = pyproj.Proj(init=p1_type)
    p2 = pyproj.Proj(init=p2_type)
    fx, fy = pyproj.transform(p1, p2, coord[:, 0], coord[:, 1],always_xy=True)
    return np.dstack([fx, fy])[0]



