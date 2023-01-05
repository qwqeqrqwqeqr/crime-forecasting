import pandas as pd

from business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from business.preprocessing.utils.utils import convert_csv, get_center_coordinate
from utils.constants import *

def service():
    pass

    # print("========== 격자 내 시설 개수를 산출 합니다. ==========")
    # #SHP 파일은 먼저 CSV로 변환한다.
    # convert_csv(PATH_아동안전지킴이시설물_ORIGIN_SHP,PATH_아동안전지킴이시설물_ORIGIN,CP_949)
    # convert_csv(PATH_편의점_ORIGIN_SHP,PATH_편의점_ORIGIN,UTF_8)
    #
    # #안전시설
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_CCTV_ORIGIN,PATH_CCTV_AFTER,CP_949,'경도','위도',EPSG_4326)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_스마트보안등_ORIGIN,PATH_스마트보안등_AFTER,UTF_8,'경도','위도',EPSG_4326)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_안심택배함_ORIGIN,PATH_여성안심택배함_AFTER,EUC_KR,'WGS X 좌표','WGS Y 좌표',EPSG_4326)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_여성안심지킴이집_ORIGIN,PATH_여성안심지킴이집_AFTER,UTF_8,'lon','lat',EPSG_4326)
    #
    #
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_아동안전지킴이시설물_ORIGIN,PATH_아동안전지킴이시설물_AFTER,EUC_KR,'x','y',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_편의점_ORIGIN,PATH_편의점_AFTER,EUC_KR,'x','y',EPSG_5181)
    #
    #
    # #위험시설
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_노래연습장_ORIGIN,PATH_노래연습장_AFTER,EUC_KR,'좌표정보(X)','좌표정보(Y)',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_단란주점_ORIGIN,PATH_단란주점_AFTER,EUC_KR,'좌표정보(X)','좌표정보(Y)',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_목욕장업_ORIGIN,PATH_목욕장업_AFTER,EUC_KR,'좌표정보(X)','좌표정보(Y)',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_숙박업_ORIGIN,PATH_숙박업_AFTER,EUC_KR,'좌표정보(X)','좌표정보(Y)',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_유흥주점_ORIGIN,PATH_유흥주점_AFTER,EUC_KR,'좌표정보(X)','좌표정보(Y)',EPSG_5181)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_인터넷컴퓨터게임시설_ORIGIN,PATH_인터넷컴퓨터게임시설_AFTER,CP_949, '좌표정보(X)','좌표정보(Y)',EPSG_5181)
    #
    # #치안시설
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_경찰서_ORIGIN,PATH_경찰서_AFTER,UTF_8,'lon','lat',EPSG_4326)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_치안센터_ORIGIN,PATH_치안센터_AFTER,UTF_8,'lon','lat',EPSG_4326)
    # count_point_in_polygon(True,PATH_격자_MAP,UTF_8,'격자고유번호',PATH_파출소지구대_ORIGIN,PATH_파출소지구대_AFTER,UTF_8,'lon','lat',EPSG_4326)
    #
    # #112신고접수
    # get_center_coordinate(pd.read_csv(PATH_112신고접수정보_ORIGIN, encoding=UTF_8),'HPPN_X_SW','HPPN_X_NE','HPPN_X_NW','HPPN_X_SE','HPPN_Y_SW','HPPN_Y_NE','HPPN_Y_NW','HPPN_Y_SE')
    # count_point_in_polygon(True,PATH_격자_MAP,CP_949,'격자고유번호',PATH_112신고접수정보_AFTER,PATH_112신고접수정보_AFTER,UTF_8,'x','y',EPSG_4326)

    # print("========== 자치구 내 시설 개수를 산출 합니다. ==========")
    # count_point_in_polygon(False,PATH_자치구_MAP,CP_949,'SGG_NM',PATH_CCTV_ORIGIN,PATH_CCTV_AFTER,EUC_KR,'경도','위도',EPSG_4326)


