import pandas as pd

from business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from business.preprocessing.utils.utils import convert_csv, get_center_coordinate
from utils.constants import *


def convert_to_grid_facility():
    print("========== 격자 내 시설 개수를 산출 합니다. ==========")
    # SHP 파일은 먼저 CSV로 변환한다.
    convert_csv(PATH_아동안전지킴이시설물_ORIGIN_SHP, PATH_아동안전지킴이시설물_ORIGIN, CP_949)
    convert_csv(PATH_편의점_ORIGIN_SHP, PATH_편의점_ORIGIN, UTF_8)

    # 안전시설
    count_point_in_polygon(True, PATH_격자_MAP, '격자고유번호', pd.read_csv(PATH_CCTV_ORIGIN, encoding=EUC_KR), PATH_CCTV_AFTER,
                           CP_949, '경도', '위도',
                           EPSG_4326)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_스마트보안등_ORIGIN, encoding=UTF_8)
                           , PATH_스마트보안등_AFTER, '경도', '위도',
                           EPSG_4326)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_안심택배함_ORIGIN, encoding=EUC_KR)
                           , PATH_여성안심택배함_AFTER,
                           'WGS X 좌표', 'WGS Y 좌표', EPSG_4326)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_여성안심지킴이집_ORIGIN, encoding=UTF_8)
                           , PATH_여성안심지킴이집_AFTER, 'lon',
                           'lat', EPSG_4326)

    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_아동안전지킴이시설물_ORIGIN, encoding=EUC_KR)
                           ,PATH_아동안전지킴이시설물_AFTER, 'x', 'y', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_편의점_ORIGIN, encoding=EUC_KR)
                           , PATH_편의점_AFTER, 'x', 'y',
                           EPSG_5181)

    # 위험시설
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_노래연습장_ORIGIN, encoding=EUC_KR)
                           , PATH_노래연습장_AFTER, '좌표정보(X)','좌표정보(Y)', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_단란주점_ORIGIN, encoding=EUC_KR)
                           , PATH_단란주점_AFTER, '좌표정보(X)',  '좌표정보(Y)', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_목욕장업_ORIGIN, encoding=EUC_KR)
                           , PATH_목욕장업_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_숙박업_ORIGIN, encoding=EUC_KR)
                           , PATH_숙박업_AFTER, '좌표정보(X)','좌표정보(Y)', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_유흥주점_ORIGIN, encoding=EUC_KR)
                           , PATH_유흥주점_AFTER, '좌표정보(X)', '좌표정보(Y)', EPSG_5181)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_인터넷컴퓨터게임시설_ORIGIN, encoding=CP_949)
                           , PATH_인터넷컴퓨터게임시설_AFTER,'좌표정보(X)', '좌표정보(Y)', EPSG_5181)

    # 치안시설
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_경찰서_ORIGIN, encoding=UTF_8)
                           , PATH_경찰서_AFTER, 'lon', 'lat', EPSG_4326)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_치안센터_ORIGIN, encoding=UTF_8)
                           , PATH_치안센터_AFTER, 'lon', 'lat', EPSG_4326)
    count_point_in_polygon(True, PATH_격자_MAP, UTF_8, '격자고유번호', pd.read_csv(PATH_파출소지구대_ORIGIN, encoding=UTF_8)
                           , PATH_파출소지구대_AFTER, 'lon','lat', EPSG_4326)

    # 112신고접수
    get_center_coordinate(pd.read_csv(PATH_112신고접수정보_ORIGIN, encoding=UTF_8), 'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW',
                          'HPPN_X_SE', 'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')

    count_point_in_polygon(True, PATH_격자_MAP, CP_949, '격자고유번호'
                           , PATH_112신고접수정보_AFTER, PATH_112신고접수정보_AFTER, UTF_8, 'x',
                           'y', EPSG_4326)


