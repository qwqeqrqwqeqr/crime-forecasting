'''
좌표정보
'''

EPSG_5181 = "epsg:5181"
EPSG_4326 = "epsg:4326"

'''
PATH
'''

PATH_ORIGIN = "data/origin/"
PATH_MAP = "data/map/"
PATH_AFTER = "data/after/"
PATH_EXPAND = "data/expand/"

"""
ORIGIN_PATH
"""

PATH_112신고접수정보_ORIGIN = PATH_ORIGIN + "report/report2021.csv"

PATH_노래연습장_ORIGIN = PATH_ORIGIN + "danger_facility/서울시노래연습장업인허가정보.csv"
PATH_단란주점_ORIGIN = PATH_ORIGIN + "danger_facility/서울시단란주점영업인허가정보.csv"
PATH_목욕장업_ORIGIN = PATH_ORIGIN + "danger_facility/서울시목욕장업인허가정보.csv"
PATH_숙박업_ORIGIN = PATH_ORIGIN + "danger_facility/서울시숙박업인허가정보.csv"
PATH_유흥주점_ORIGIN = PATH_ORIGIN + "danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_인터넷컴퓨터게임시설_ORIGIN = PATH_ORIGIN + "danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"

PATH_경찰서_ORIGIN = PATH_ORIGIN + "police_facility/경찰서.csv"
PATH_치안센터_ORIGIN = PATH_ORIGIN + "police_facility/치안센터.csv"
PATH_파출소지구대_ORIGIN = PATH_ORIGIN + "police_facility/파출소지구대.csv"

PATH_CCTV_ORIGIN = PATH_ORIGIN + "safety_facility/서울시_CCTV_설치현황.csv"
PATH_스마트보안등_ORIGIN = PATH_ORIGIN + "safety_facility/스마트보안등.csv"
PATH_안심택배함_ORIGIN = PATH_ORIGIN + "safety_facility/여성안심택배함.csv"
PATH_여성안심지킴이집_ORIGIN = PATH_ORIGIN + "safety_facility/여성안심지킴이집.csv"
PATH_아동안전지킴이시설물_ORIGIN = PATH_ORIGIN + "safety_facility/아동안전지킴이시설물.csv"
PATH_편의점_ORIGIN = PATH_ORIGIN + "safety_facility/편의점.csv"

PATH_아동안전지킴이시설물_ORIGIN_SHP = PATH_ORIGIN + "safety_facility/아동안전지킴이시설물.shp"
PATH_편의점_ORIGIN_SHP = PATH_ORIGIN + "safety_facility/편의점.shp"

'''
MAP_PATH
'''

PATH_격자_MAP = PATH_MAP + "격자.geojson"
PATH_집계구_MAP = PATH_MAP + "집계구.shp"
PATH_파출소지구대_MAP = PATH_MAP + "경찰서별파출소지구대위치정보.shp"
PATH_한강수변구역_MAP = PATH_MAP + "한강수변구역.shp"
PATH_행정구역_MAP = PATH_MAP + "행정구역.shp"

'''
AFTER_PATH
'''
PATH_경찰서_AFTER = PATH_AFTER + "police_facility/경찰서.csv"
PATH_치안센터_AFTER = PATH_AFTER + "police_facility/치안센터.csv"
PATH_파출소지구대_AFTER = PATH_AFTER + "police_facility/파출소지구대.csv"

PATH_CCTV_AFTER = PATH_AFTER + "safety_facility/서울시_CCTV_설치현황.csv"
PATH_스마트보안등_AFTER = PATH_AFTER + "safety_facility/스마트보안등.csv"
PATH_여성안심택배함_AFTER = PATH_AFTER + "safety_facility/여성안심택배함.csv"
PATH_여성안심지킴이집_AFTER = PATH_AFTER + "safety_facility/여성안심지킴이집.csv"

PATH_아동안전지킴이시설물_AFTER = PATH_AFTER + "safety_facility/아동안전지킴이시설물.csv"
PATH_편의점_AFTER = PATH_AFTER + "safety_facility/편의점.csv"

PATH_노래연습장_AFTER = PATH_AFTER + "danger_facility/서울시노래연습장업인허가정보.csv"
PATH_단란주점_AFTER = PATH_AFTER + "danger_facility/서울시단란주점영업인허가정보.csv"
PATH_목욕장업_AFTER = PATH_AFTER + "danger_facility/서울시목욕장업인허가정보.csv"
PATH_숙박업_AFTER = PATH_AFTER + "danger_facility/서울시숙박업인허가정보.csv"
PATH_유흥주점_AFTER = PATH_AFTER + "danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_인터넷컴퓨터게임시설_AFTER = PATH_AFTER + "danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"

'''
EXPAND_PATH
'''

PATH_여성안심지킴이집_EXPAND = PATH_EXPAND + "여성안심지킴이집.csv"
PATH_여성안심택배함_EXPAND = PATH_EXPAND + "여성안심택배함.csv"
PATH_아동안전지킴이시설물_EXPAND = PATH_EXPAND + "아동안전지킴이시설물.csv"
PATH_편의점_EXPAND = PATH_EXPAND + "편의점.csv"

PATH_경찰서_EXPAND = PATH_EXPAND + "경찰서.csv"
PATH_치안센터_EXPAND = PATH_EXPAND + "치안센터.csv"
PATH_파출소지구대_EXPAND = PATH_EXPAND + "파출소지구대.csv"

'''
PATH_LIST
'''

PATH_LIST = [PATH_ORIGIN,

             PATH_MAP,
             PATH_AFTER,
             PATH_EXPAND,
             PATH_ORIGIN+"report/",
             PATH_ORIGIN+"danger_facility/",
             PATH_ORIGIN+"police_facility/",
             PATH_ORIGIN+"safety_facility/",

             PATH_AFTER+"data/after/report/",
             PATH_AFTER+"data/after/danger_facility/",
             PATH_AFTER+"data/after/safety_facility/",
             PATH_AFTER+"data/after/danger_facility/",
             ]

FILE_LIST = [
    PATH_112신고접수정보_ORIGIN,

    PATH_노래연습장_ORIGIN,
    PATH_단란주점_ORIGIN,
    PATH_목욕장업_ORIGIN,
    PATH_숙박업_ORIGIN,
    PATH_유흥주점_ORIGIN,
    PATH_인터넷컴퓨터게임시설_ORIGIN,

    PATH_경찰서_ORIGIN,
    PATH_치안센터_ORIGIN,
    PATH_파출소지구대_ORIGIN,

    PATH_CCTV_ORIGIN,
    PATH_스마트보안등_ORIGIN,
    PATH_안심택배함_ORIGIN,
    PATH_여성안심지킴이집_ORIGIN,
    PATH_아동안전지킴이시설물_ORIGIN_SHP,
    PATH_편의점_ORIGIN_SHP,

    PATH_격자_MAP,
]
