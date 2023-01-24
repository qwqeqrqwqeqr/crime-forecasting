import os

import pandas as pd

from app.business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from app.business.preprocessing.expand_data.expand_data import expand_data
from app.business.preprocessing.utils.utils import get_center_coordinate
from app.utils import *
from app.utils.constants import *
import geopandas as gpd


def convert_to_grid_facility(df_list, expand_flag, depth):
    print("격자 별 시설 개수를 산출 합니다.")
    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")

    # 안전시설
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_CCTV_ORIGIN, encoding=EUC_KR),
                               PATH_CCTV_AFTER, '경도', '위도', EPSG_4326,True))
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SMART_SECURITY_LIGHT_ORIGIN, encoding=UTF_8)
                               , PATH_SMART_SECURITY_LIGHT_AFTER, '경도', '위도', EPSG_4326,True))
    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_CONVENIENCE_STORE_ORIGIN, encoding=EUC_KR)
                                   , PATH_CONVENIENCE_STORE_AFTER, 'x', 'y', EPSG_5181,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_CONVENIENCE_STORE_ORIGIN, encoding=EUC_KR)
                               , PATH_CONVENIENCE_STORE_AFTER, 'x', 'y', EPSG_5181, True)
        df_list.append(expand_data(depth, PATH_CONVENIENCE_STORE_AFTER, PATH_CONVENIENCE_STORE_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SAFETY_HOUSE_ORIGIN, encoding=UTF_8)
                                   , PATH_SAFETY_HOUSE_AFTER, 'lon', 'lat', EPSG_4326,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SAFETY_HOUSE_ORIGIN, encoding=UTF_8)
                               , PATH_SAFETY_HOUSE_AFTER, 'lon', 'lat', EPSG_4326, True)
        df_list.append(expand_data(depth, PATH_SAFETY_HOUSE_AFTER, PATH_SAFETY_HOUSE_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_DELIVERY_BOX_ORIGIN, encoding=EUC_KR)
                                   , PATH_DELIVERY_BOX_AFTER, 'WGS X 좌표', 'WGS Y 좌표', EPSG_4326,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_DELIVERY_BOX_ORIGIN, encoding=EUC_KR)
                               , PATH_DELIVERY_BOX_AFTER, 'WGS X 좌표', 'WGS Y 좌표', EPSG_4326, True)
        df_list.append(expand_data(depth, PATH_DELIVERY_BOX_AFTER, PATH_DELIVERY_BOX_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호',
                                   pd.read_csv(PATH_SAFETY_FACILITY_ORIGIN, encoding=EUC_KR)
                                   , PATH_SAFETY_FACILITY_AFTER, 'x', 'y', EPSG_5181,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호',
                               pd.read_csv(PATH_SAFETY_FACILITY_ORIGIN, encoding=EUC_KR)
                               , PATH_SAFETY_FACILITY_AFTER, 'x', 'y', EPSG_5181, True)
        df_list.append(
            expand_data(depth, PATH_SAFETY_FACILITY_AFTER, PATH_SAFETY_FACILITY_AFTER, UTF_8))

    # 위험시설
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_ICG_ORIGIN, encoding=CP_949)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_NY_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_DJ_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_YH_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_MJ_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SB_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181,True))

    # 치안시설
    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_POICE_STATION_ORIGIN, encoding=UTF_8)
                                   , 'lon', 'lat', EPSG_4326,True))
    else:
         count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_POICE_STATION_ORIGIN, encoding=UTF_8)
                               , 'lon', 'lat', EPSG_4326, True)
         df_list.append(expand_data(depth, PATH_POLICE_STATION_AFTER, PATH_POLICE_STATION_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SAFETY_CENTER_ORIGIN, encoding=UTF_8)
                                   , 'lon', 'lat', EPSG_4326,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SAFETY_CENTER_ORIGIN, encoding=UTF_8)
                               , 'lon', 'lat', EPSG_4326, True)
        df_list.append( expand_data(depth, PATH_SAFETY_CENTER_AFTER, PATH_SAFETY_CENTER_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_POLICE_OFFICE_ORIGIN, encoding=UTF_8)
                                   , 'lon', 'lat', EPSG_4326,True))
    else:
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_POLICE_OFFICE_ORIGIN, encoding=UTF_8)
                               , 'lon', 'lat', EPSG_4326, True)
        df_list.append( expand_data(depth, PATH_POLICE_OFFICE_AFTER, PATH_POLICE_OFFICE_AFTER, UTF_8))


    return df_list






# 112신고 접수
def convert_to_grid_report(grid_map):
    print("격자 별 신고 건수를 산출 합니다.")
    return count_point_in_polygon(grid_map, '격자고유번호'
                                  ,
                                  get_center_coordinate(pd.read_csv(PATH_112신고접수정보_ORIGIN, encoding=UTF_8),
                                                        'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                                                        'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')
                                  , 'x', 'y', EPSG_4326,False)


# 생활인구
def convert_to_grid_life_population():
    print("격자 별 생활 인구를 산출 합니다.")
    area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)
    life_population_df = pd.read_csv(PATH_LIFE_POPULATION_AFTER + os.listdir(PATH_LIFE_POPULATION_AFTER)[0],
                                     encoding=UTF_8)

    # 집계구 별 격자랑 매핑
    grid_time_life_population_map = pd.merge(area_map, life_population_df, left_on='TOT_REG_CD',
                                             right_on='집계구코드', how='inner')

    grid_time_life_population_map['count'] = grid_time_life_population_map['총생활인구수'] / grid_time_life_population_map[
        'duplicate']
    return grid_time_life_population_map[['격자고유번호', 'count']]
