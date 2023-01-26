
import pandas as pd

from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
from app.business.preprocessing.expand_data import expand_data
from app.utils.constants import *
import geopandas as gpd


def concat_grid_facility(df_list, depth):
    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_CCTV_ORIGIN, encoding=EUC_KR),
                               '경도', '위도', EPSG_4326, True))
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SMART_SECURITY_LIGHT_ORIGIN, encoding=UTF_8)
                               , '경도', '위도', EPSG_4326, True))

    df_list.append(
        expand_data(depth,
                    count_point_in_polygon(grid_map, '격자고유번호',
                                           pd.read_csv(PATH_CONVENIENCE_STORE_ORIGIN, encoding=EUC_KR)
                                           , 'x', 'y', EPSG_5181, True)))

    df_list.append(
        expand_data(depth,
                    count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SAFETY_HOUSE_ORIGIN, encoding=UTF_8)
                                           , 'lon', 'lat', EPSG_4326, True)))

    df_list.append(
        expand_data(depth,
                    count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_DELIVERY_BOX_ORIGIN, encoding=EUC_KR)
                                           , 'WGS X 좌표', 'WGS Y 좌표', EPSG_4326, True)))

    df_list.append(
        expand_data(depth,
                    count_point_in_polygon(grid_map, '격자고유번호',
                                           pd.read_csv(PATH_SAFETY_FACILITY_ORIGIN, encoding=EUC_KR)
                                           , 'x', 'y', EPSG_5181, True)))

    # 위험시설
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_ICG_ORIGIN, encoding=CP_949)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_NY_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_DJ_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_YH_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))

    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_MJ_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))
    df_list.append(
        count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_SB_ORIGIN, encoding=EUC_KR)
                               , '좌표정보(X)', '좌표정보(Y)', EPSG_5181, True))

    # 치안시설

    df_list.append(expand_data(depth, count_point_in_polygon(grid_map, '격자고유번호',
                                                             pd.read_csv(PATH_POICE_STATION_ORIGIN, encoding=UTF_8)
                                                             , 'lon', 'lat', EPSG_4326, True)))

    df_list.append(expand_data(depth, count_point_in_polygon(grid_map, '격자고유번호',
                                                             pd.read_csv(PATH_SAFETY_CENTER_ORIGIN, encoding=UTF_8)
                                                             , 'lon', 'lat', EPSG_4326, True)))

    df_list.append(expand_data(depth,     count_point_in_polygon(grid_map, '격자고유번호', pd.read_csv(PATH_POLICE_OFFICE_ORIGIN, encoding=UTF_8)

                                                                 , 'lon', 'lat', EPSG_4326, True)))

    return df_list
# 생활인구

