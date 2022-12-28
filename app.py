from business.preprocessing.count_point_in_polygon.security_related_industries.count_point_in_polygon import count_point_in_polygon
from util.constants import *

EPSG_5181 = "epsg:5181"
EPSG_4326 = "epsg:4326"
if __name__ == '__main__':
    print(1)
    DEPTH =2


    # count_point_in_polygon(PATH_노래연습장_ORIGIN,PATH_노래연습장_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_단란주점_ORIGIN,PATH_단란주점_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_목욕장업_ORIGIN,PATH_목욕장업_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_숙박업_ORIGIN,PATH_숙박업_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_유흥주점_ORIGIN,PATH_유흥주점_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    count_point_in_polygon(PATH_인터넷컴퓨터게임시설_ORIGIN,PATH_인터넷컴퓨터게임시설_AFTER,'cp949','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)


    # count_point_in_polygon(PATH_경찰서_ORIGIN,PATH_경찰서_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_치안센터_ORIGIN,PATH_치안센터_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_파출소지구대_ORIGIN,PATH_파출소지구대_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)

    # expand_data(DEPTH,PATH_여성안심지킴이집_AFTER,PATH_여성안심지킴이집_EXPAND)
    # expand_data(DEPTH,PATH_여성안심택배함_AFTER,PATH_여성안심택배함_EXPAND)
    # expand_data(DEPTH,PATH_아동안전지킴이시설물_AFTER,PATH_아동안전지킴이시설물_EXPAND)
    # expand_data(DEPTH,PATH_편의점_AFTER,PATH_편의점_EXPAND)
