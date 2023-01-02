import geopandas as gpd
import pandas as pd
import numpy as np
from geopandas import GeoDataFrame
from pyproj import transform, Proj


'''
Param
count_point_in_polygon
    geojson_type => geojson : True /  shape : False
    map_path => 맵 경로
    map_encoding=> 맵 인코딩 방식
    map_key => 매핑하기위한 맵의 키 (ex. 격자고유번호)
    input_path => 데이터 입력경로
    output_path => 데이터 저장경로
    encoding => 인코딩 방식
    x_coordinate_name =>  x 좌표 이름
    y_coordinate_name =>  y 좌표 이름
    current_coordinate_system => 현재 좌표계
'''

GEO_JSON_DRIVER= "GeoJSON"

def count_point_in_polygon(geojson_type, map_path,map_encoding,map_key,input_path, output_path, encoding, x_coordinate_name, y_coordinate_name, current_coordinate_system):

   #geojson 파일과 shp 파일에 따라 다르게 처리한다.
    if geojson_type:
        grid_geojson = gpd.read_file(map_path, driver=GEO_JSON_DRIVER)
    else:
        grid_geojson = gpd.read_file(map_path, encoding=map_encoding)


    # csv 파일을 읽고 공통적으로 처리하기 위해 x y 컬럼을 생성해줍니다.
    df = pd.read_csv(input_path, encoding=encoding)
    df['x'] = df[x_coordinate_name]
    df['y'] = df[y_coordinate_name]


    #좌표계를 뱐환합니다.
    transform_coordinate_result = transform_coordinate(np.array(df[['x', 'y']]), current_coordinate_system, grid_geojson.crs)
    df['x'] = transform_coordinate_result[:, 0]
    df['y'] = transform_coordinate_result[:, 1]

    df = df[['x', 'y']]

    # x y 제외 나머지 컬럼을 삭제한 뒤, 중복을 제거합니다.
    df = df.drop_duplicates()

    # polygon 과 point의 교집합을 구합니다. (polygon 내 point를 산출하기위함)
    point = GeoDataFrame(df, geometry=gpd.points_from_xy(x=df.x, y=df.y))
    point.crs = grid_geojson.crs
    point_in_polygon = gpd.sjoin(point, grid_geojson[[map_key, 'geometry']], how="inner", predicate='intersects')

    # polygon 별 group by 를 진행합니다.
    count_result = count_in_df(point_in_polygon,map_key)

    # point가 할당되지 않은 polygon과 할당된 polygon을 중첩시킵니다.
    concat_result = concat_df(count_result, grid_geojson,map_key)

    # 파일을 csv 형태로 저장합니다.
    concat_result.to_csv(output_path, index=False)


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
