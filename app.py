from util.util import init

if __name__ == '__main__':

    DEPTH =2

    init()


    # #SHP 파일은 CSV로 변환한다.
    # convert_csv(PATH_아동안전지킴이시설물_ORIGIN_SHP,PATH_아동안전지킴이시설물_ORIGIN,'CP949')
    # convert_csv(PATH_편의점_ORIGIN_SHP,PATH_편의점_ORIGIN,'utf-8')
    #
    # count_point_in_polygon(PATH_CCTV_ORIGIN,PATH_CCTV_AFTER,'CP949','경도','위도',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_스마트보안등_ORIGIN,PATH_스마트보안등_AFTER,'utf-8','경도','위도',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_안심택배함_ORIGIN,PATH_여성안심택배함_AFTER,'euc-kr','WGS X 좌표','WGS Y 좌표',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_여성안심지킴이집_ORIGIN,PATH_여성안심지킴이집_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    #
    #
    # count_point_in_polygon(PATH_아동안전지킴이시설물_ORIGIN,PATH_아동안전지킴이시설물_AFTER,'euc-kr','x','y',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_편의점_ORIGIN,PATH_편의점_AFTER,'euc-kr','x','y',EPSG_5181,EPSG_4326)
    #
    #
    # count_point_in_polygon(PATH_노래연습장_ORIGIN,PATH_노래연습장_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_단란주점_ORIGIN,PATH_단란주점_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_목욕장업_ORIGIN,PATH_목욕장업_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_숙박업_ORIGIN,PATH_숙박업_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_유흥주점_ORIGIN,PATH_유흥주점_AFTER,'euc-kr','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    # count_point_in_polygon(PATH_인터넷컴퓨터게임시설_ORIGIN,PATH_인터넷컴퓨터게임시설_AFTER,'cp949','좌표정보(X)','좌표정보(Y)',EPSG_5181,EPSG_4326)
    #
    # count_point_in_polygon(PATH_경찰서_ORIGIN,PATH_경찰서_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_치안센터_ORIGIN,PATH_치안센터_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    # count_point_in_polygon(PATH_파출소지구대_ORIGIN,PATH_파출소지구대_AFTER,'utf-8','lon','lat',EPSG_4326,EPSG_4326)
    #
    #
    #
    # expand_data(DEPTH,PATH_여성안심지킴이집_AFTER,PATH_여성안심지킴이집_EXPAND,'euc-kr')
    # expand_data(DEPTH,PATH_여성안심택배함_AFTER,PATH_여성안심택배함_EXPAND,'euc-kr')
    # expand_data(DEPTH,PATH_아동안전지킴이시설물_AFTER,PATH_아동안전지킴이시설물_EXPAND,'euc-kr')
    # expand_data(DEPTH,PATH_편의점_AFTER,PATH_편의점_EXPAND,'euc-kr')
    #
    # expand_data(DEPTH,PATH_경찰서_AFTER,PATH_경찰서_EXPAND,'utf-8')
    # expand_data(DEPTH,PATH_치안센터_AFTER,PATH_치안센터_EXPAND,'utf-8')
    # expand_data(DEPTH,PATH_파출소지구대_AFTER,PATH_파출소지구대_EXPAND,'utf-8')
