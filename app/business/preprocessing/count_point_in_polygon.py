# -*- coding: utf-8 -*-
import numpy as np

'''
Param
- polygon : target polygon
- polygon_key : polygon key to map (ex. 격자고유번호)
- df : target point
- x_coordinate_name : x coordinate column name
- y_coordinate_name : y coordinate column name
- df_coordinate_system : df coordinate system
- duplicate_flag : [True] Remove duplicates / [False] not remove duplicates
'''


def count_point_in_polygon(polygon, polygon_key, df, x_coordinate_name, y_coordinate_name, df_coordinate_system,
                           duplicate_flag):
    df['x'] = df[x_coordinate_name]
    df['y'] = df[y_coordinate_name]

    transform_coordinate_result = transform_coordinate(np.array(df[['x', 'y']]), df_coordinate_system, polygon.crs)
    df['x'] = transform_coordinate_result[:, 0]
    df['y'] = transform_coordinate_result[:, 1]

    df = df[['x', 'y']]  # create point list

    if duplicate_flag:
        df = df.drop_duplicates()  # remove duplicates

    import geopandas as gpd
    point = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df.x, y=df.y))
    point.crs = polygon.crs
    point_in_polygon = gpd.sjoin(point, polygon[[polygon_key, 'geometry']], how="inner",
                                 predicate='intersects')  # intersect polygon and point

    count_result = count_in_df(point_in_polygon, polygon_key)  # counting point in polygon and sum this

    concat_result = concat_df(count_result, polygon, polygon_key)  # concat polygon with points and without any point

    return concat_result


def concat_df(point_df, full_df, map_key):  # concat polygon with points and without any point
    import pandas as pd

    not_point_df = pd.DataFrame(
        {map_key: list(list(set(full_df[map_key].to_list()) - set(point_df[map_key].to_list())))})
    not_point_df['count'] = 0
    not_point_df = pd.concat([point_df, not_point_df])

    return not_point_df[[map_key, 'count']]


def count_in_df(df, map_key):  # counting point in polygon and sum this
    df['count'] = 1
    return df.groupby([map_key]).sum(numeric_only=True).reset_index()


from pyproj import transform, Proj


def transform_coordinate(coord, p1_type, p2_type):  # transform coordinate
    p1 = Proj(init=p1_type)
    p2 = Proj(init=p2_type)
    fx, fy = transform(p1, p2, coord[:, 0], coord[:, 1])
    return np.dstack([fx, fy])[0]
