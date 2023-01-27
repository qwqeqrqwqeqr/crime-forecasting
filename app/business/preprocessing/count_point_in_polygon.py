# -*- coding: utf-8 -*-

import geopandas as gpd
import pandas as pd
import numpy as np
from geopandas import GeoDataFrame
from pyproj import transform, Proj


'''
Param
    map => map geojson 데이터
    map_key => 매핑하기위한 맵의 키 (ex. 격자고유번호)
    df => 입력 데이터 프레임
    x_coordinate_name =>  x 좌표 이름
    y_coordinate_name =>  y 좌표 이름
    current_coordinate_system => 현재 좌표계
    duplicate_flag=> 제거 : True / 미제거 : False
'''

GEO_JSON_DRIVER= "GeoJSON"


def count_point_in_polygon(map,map_key,df, x_coordinate_name, y_coordinate_name, current_coordinate_system,duplicate_flag):


    df['x'] = df[x_coordinate_name]
    df['y'] = df[y_coordinate_name]

    #좌표계를 뱐환합니다.
    transform_coordinate_result = transform_coordinate(np.array(df[['x', 'y']]), current_coordinate_system, map.crs)
    df['x'] = transform_coordinate_result[:, 0]
    df['y'] = transform_coordinate_result[:, 1]

    df = df[['x', 'y']]

    # x y 제외 나머지 컬럼을 삭제한 뒤, 중복을 제거합니다.
    if duplicate_flag:
     df = df.drop_duplicates()



    # polygon 과 point의 교집합을 구합니다. (polygon 내 point를 산출하기위함)
    point = GeoDataFrame(df, geometry=gpd.points_from_xy(x=df.x, y=df.y))
    point.crs = map.crs
    point_in_polygon = gpd.sjoin(point, map[[map_key, 'geometry']], how="inner", predicate='intersects')

    # polygon 별 group by 를 진행합니다.
    count_result = count_in_df(point_in_polygon,map_key)


    # point가 할당되지 않은 polygon과 할당된 polygon을 중첩시킵니다.
    concat_result = concat_df(count_result, map,map_key)


    return concat_result


def concat_df(subset_df, full_df,map_key):
    subset_df_grid_list = subset_df[map_key].to_list()
    full_df_grid_list = full_df[map_key].to_list()

    temp_df = pd.DataFrame({map_key: list(list(set(full_df_grid_list) - set(subset_df_grid_list)))})
    temp_df['count'] = 0

    crime_count_full = pd.concat([subset_df, temp_df])

    return crime_count_full[[map_key, 'count']]


#group by
def count_in_df(df,map_key):
    df['count'] = 1
    return df.groupby([map_key]).sum(numeric_only=True).reset_index()


#좌표계변환
def transform_coordinate(coord, p1_type, p2_type):
    p1 = Proj(init=p1_type)
    p2 = Proj(init=p2_type)
    fx, fy = transform(p1, p2, coord[:, 0], coord[:, 1])
    return np.dstack([fx, fy])[0]
