'''
좌표정보
'''

EPSG_5181 = "epsg:5181"
EPSG_4326 = "epsg:4326"




"""
ORIGIN_PATH
"""

PATH_112신고접수정보_ORIGIN="data/origin/report/112신고접수정보.csv"

PATH_노래연습장_ORIGIN="data/origin/danger_facility/서울시노래연습장업인허가정보.csv"
PATH_단란주점_ORIGIN="data/origin/danger_facility/서울시단란주점영업인허가정보.csv"
PATH_목욕장업_ORIGIN="data/origin/danger_facility/서울시목욕장업인허가정보.csv"
PATH_숙박업_ORIGIN="data/origin/danger_facility/서울시숙박업인허가정보.csv"
PATH_유흥주점_ORIGIN="data/origin/danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_인터넷컴퓨터게임시설_ORIGIN="data/origin/danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"

PATH_경찰서_ORIGIN = "data/origin/police_facility/경찰서.csv"
PATH_치안센터_ORIGIN = "data/origin/police_facility/치안센터.csv"
PATH_파출소지구대_ORIGIN= "data/origin/police_facility/파출소지구대.csv"

PATH_CCTV_ORIGIN="data/origin/safety_facility/서울시_CCTV_설치현황.csv"
PATH_스마트보안등_ORIGIN="data/origin/safety_facility/스마트보안등.csv"
PATH_안심택배함_ORIGIN="data/origin/safety_facility/여성안심택배함.csv"
PATH_여성안심지킴이집_ORIGIN="data/origin/safety_facility/여성안심지킴이집.csv"
PATH_아동안전지킴이시설물_ORIGIN="data/origin/safety_facility/아동안전지킴이시설물.csv"
PATH_편의점_ORIGIN="data/origin/safety_facility/편의점.csv"

PATH_아동안전지킴이시설물_ORIGIN_SHP="data/origin/safety_facility/아동안전지킴이시설물.shp"
PATH_편의점_ORIGIN_SHP="data/origin/safety_facility/편의점.shp"


'''
MAP_PATH
'''

PATH_격자_MAP="data/map/격자.geojson"
PATH_집계구_MAP="data/map/집계구.shp"
PATH_파출소지구대_MAP="data/map/경찰서별파출소지구대위치정보.shp"
PATH_한강수변구역_MAP="data/map/한강수변구역.shp"
PATH_행정구역_MAP="data/map/행정구역.shp"



'''
AFTER_PATH
'''
PATH_경찰서_AFTER = "data/after/police_facility/경찰서.csv"
PATH_치안센터_AFTER = "data/after/police_facility/치안센터.csv"
PATH_파출소지구대_AFTER= "data/after/police_facility/파출소지구대.csv"


PATH_CCTV_AFTER="data/after/safety_facility/서울시_CCTV_설치현황.csv"
PATH_스마트보안등_AFTER="data/after/safety_facility/스마트보안등.csv"
PATH_여성안심택배함_AFTER = "data/after/safety_facility/여성안심택배함.csv"
PATH_여성안심지킴이집_AFTER = "data/after/safety_facility/여성안심지킴이집.csv"

PATH_아동안전지킴이시설물_AFTER= "data/after/safety_facility/아동안전지킴이시설물.csv"
PATH_편의점_AFTER= "data/after/safety_facility/편의점.csv"


PATH_노래연습장_AFTER="data/after/danger_facility/서울시노래연습장업인허가정보.csv"
PATH_단란주점_AFTER="data/after/danger_facility/서울시단란주점영업인허가정보.csv"
PATH_목욕장업_AFTER="data/after/danger_facility/서울시목욕장업인허가정보.csv"
PATH_숙박업_AFTER="data/after/danger_facility/서울시숙박업인허가정보.csv"
PATH_유흥주점_AFTER="data/after/danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_인터넷컴퓨터게임시설_AFTER="data/after/danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"


'''
EXPAND_PATH
'''

PATH_여성안심지킴이집_EXPAND = "data/expand/여성안심지킴이집.csv"
PATH_여성안심택배함_EXPAND = "data/expand/여성안심택배함.csv"
PATH_아동안전지킴이시설물_EXPAND= "data/expand/아동안전지킴이시설물.csv"
PATH_편의점_EXPAND= "data/expand/편의점.csv"

PATH_경찰서_EXPAND = "data/expand/경찰서.csv"
PATH_치안센터_EXPAND = "data/expand/치안센터.csv"
PATH_파출소지구대_EXPAND= "data/expand/파출소지구대.csv"



'''
PATH_LIST
'''


PATH_LIST = ["data/origin/",

             "data/map/",
             "data/after/",
             "data/expand/"
             "data/origin/report/",
             "data/origin/danger_facility/",
             "data/origin/police_facility/",
             "data/origin/safety_facility/",

             "data/after/report/",
             "data/after/danger_facility/",
             "data/after/safety_facility/",
             "data/after/danger_facility/",
            ]

FILE_LIST = [
    "PATH_112신고접수정보_ORIGIN",

    "PATH_노래연습장_ORIGIN",
    "PATH_단란주점_ORIGIN",
    "PATH_목욕장업_ORIGIN",
    "PATH_숙박업_ORIGIN",
    "PATH_유흥주점_ORIGIN",
    "PATH_인터넷컴퓨터게임시설_ORIGIN",

    "PATH_경찰서_ORIGIN",
    "PATH_치안센터_ORIGIN",
    "PATH_파출소지구대_ORIGIN",

    "PATH_CCTV_ORIGIN",
    "PATH_스마트보안등_ORIGIN",
    "PATH_안심택배함_ORIGIN",
    "PATH_여성안심지킴이집_ORIGIN",
    "PATH_아동안전지킴이시설물_ORIGIN_SHP",
    "PATH_편의점_ORIGIN_SHP",

    "PATH_격자_MAP",
]