import os

import pandas as pd

from business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from business.preprocessing.expand_data.expand_data import expand_data
from business.preprocessing.utils.utils import convert_csv, get_center_coordinate
from utils.constants import *


def convert_to_grid_facility(df_list, expand_flag, depth):


    print("격자 별 시설 개수를 산출 합니다.")
    # SHP 파일은 먼저 CSV로 변환한다.
    convert_csv(PATH_아동안전지킴이시설물_ORIGIN_SHP, PATH_아동안전지킴이시설물_ORIGIN, CP_949)
    convert_csv(PATH_편의점_ORIGIN_SHP, PATH_편의점_ORIGIN, UTF_8)

    # 안전시설
    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, CP_949, '격자고유번호', pd.read_csv(PATH_CCTV_ORIGIN, encoding=EUC_KR),
                               PATH_CCTV_AFTER, '경도', '위도', EPSG_4326))
    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_스마트보안등_ORIGIN, encoding=UTF_8)
                               , PATH_스마트보안등_AFTER, '경도', '위도', EPSG_4326))
    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_편의점_ORIGIN, encoding=EUC_KR)
                                   , PATH_편의점_AFTER, 'x', 'y', EPSG_5181))
    else:
        df_list.append(expand_data(depth, PATH_편의점_AFTER, PATH_편의점_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_여성안심지킴이집_ORIGIN, encoding=UTF_8)
                                   , PATH_여성안심지킴이집_AFTER, 'lon', 'lat', EPSG_4326))
    else:
        df_list.append(expand_data(depth, PATH_여성안심지킴이집_AFTER, PATH_여성안심지킴이집_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_안심택배함_ORIGIN, encoding=EUC_KR)
                                   , PATH_여성안심택배함_AFTER, 'WGS X 좌표', 'WGS Y 좌표', EPSG_4326))
    else:
        df_list.append(expand_data(depth, PATH_여성안심택배함_AFTER, PATH_여성안심택배함_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호',
                                   pd.read_csv(PATH_아동안전지킴이시설물_ORIGIN, encoding=EUC_KR)
                                   , PATH_아동안전지킴이시설물_AFTER, 'x', 'y', EPSG_5181))
    else:
        df_list.append(
            expand_data(depth, PATH_아동안전지킴이시설물_AFTER, PATH_아동안전지킴이시설물_AFTER, UTF_8))

    # 위험시설
    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_인터넷컴퓨터게임시설_ORIGIN, encoding=CP_949)
                               , PATH_인터넷컴퓨터게임시설_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))

    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_노래연습장_ORIGIN, encoding=EUC_KR)
                               , PATH_노래연습장_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))

    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_단란주점_ORIGIN, encoding=EUC_KR)
                               , PATH_단란주점_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))

    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_유흥주점_ORIGIN, encoding=EUC_KR)
                               , PATH_유흥주점_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))

    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_목욕장업_ORIGIN, encoding=EUC_KR)
                               , PATH_목욕장업_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))
    df_list.append(
        count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_숙박업_ORIGIN, encoding=EUC_KR)
                               , PATH_숙박업_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181))

    # 치안시설
    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_파출소지구대_ORIGIN, encoding=UTF_8)
                                   , PATH_파출소지구대_AFTER, 'lon', 'lat', EPSG_4326))
    else:
         df_list.append(expand_data(depth, PATH_파출소지구대_AFTER, PATH_파출소지구대_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_치안센터_ORIGIN, encoding=UTF_8)
                                   , PATH_치안센터_AFTER, 'lon', 'lat', EPSG_4326))
    else:
        df_list.append( expand_data(depth, PATH_치안센터_AFTER, PATH_치안센터_AFTER, UTF_8))

    if expand_flag:
        df_list.append(
            count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_경찰서_ORIGIN, encoding=UTF_8)
                                   , PATH_경찰서_AFTER, 'lon', 'lat', EPSG_4326))
    else:
        df_list.append( expand_data(depth, PATH_경찰서_AFTER, PATH_경찰서_AFTER, UTF_8))


    return df_list






# 112신고 접수
def convert_to_grid_report():
    print("격자 별 신고 건수를 산출 합니다.")
    return count_point_in_polygon(True, PATH_격자_MAP, CP_949, '격자고유번호'
                                  ,
                                  get_center_coordinate(pd.read_csv(PATH_112신고접수정보_ORIGIN, encoding=UTF_8),
                                                        'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                                                        'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')
                                  , PATH_112신고접수정보_AFTER, 'x', 'y', EPSG_4326)


# 생활인구
def convert_to_grid_life_population():
    print("격자 별 생활 인구를 산출 합니다.")
    area_map = pd.read_csv(PATH_격자_집계구_MAP, encoding=UTF_8)
    life_population_df = pd.read_csv(PATH_LIFE_POPULATION_AFTER + os.listdir(PATH_LIFE_POPULATION_AFTER)[0],
                                     encoding=UTF_8)

    # 집계구 별 격자랑 매핑
    grid_time_life_population_map = pd.merge(area_map, life_population_df, left_on='TOT_REG_CD',
                                             right_on='집계구코드', how='inner')

    grid_time_life_population_map['count'] = grid_time_life_population_map['총생활인구수'] / grid_time_life_population_map[
        'duplicate']
    return grid_time_life_population_map[['격자고유번호', 'count']]
