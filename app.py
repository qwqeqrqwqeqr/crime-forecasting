from business.expand_data.expand_data import expand_data
from business.preprocessing.map_origin_data.count_point_in_polygon import count_point_in_polygon
from util.constants import *

if __name__ == '__main__':
    print(1)
    DEPTH =2

    count_point_in_polygon(PATH_노래연습장_ORIGIN,PATH_노래연습장_AFTER)
    count_point_in_polygon(PATH_단란주점_ORIGIN,PATH_단란주점_AFTER)
    count_point_in_polygon(PATH_목욕장업_ORIGIN,PATH_목욕장업_AFTER)
    count_point_in_polygon(PATH_숙박업_ORIGIN,PATH_숙박업_AFTER)
    count_point_in_polygon(PATH_유흥주점_ORIGIN,PATH_유흥주점_AFTER)
    count_point_in_polygon(PATH_인터넷컴퓨터게임시설_ORIGIN,PATH_인터넷컴퓨터게임시설_AFTER)

    # expand_data(DEPTH,PATH_112신고접수여성안심지킴이집_AFTER,PATH_112신고접수여성안심지킴이집_EXPAND)
    # expand_data(DEPTH,PATH_112신고접수여성안심택배함_AFTER,PATH_112신고접수여성안심택배함_EXPAND)
    # expand_data(DEPTH,PATH_112신고접수아동안전지킴이시설물_AFTER,PATH_112신고접수아동안전지킴이시설물_EXPAND)
    # expand_data(DEPTH,PATH_112신고접수편의점_AFTER,PATH_112신고접수편의점_EXPAND)
