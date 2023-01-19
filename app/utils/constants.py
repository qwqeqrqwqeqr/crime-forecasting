
'''
좌표정보
'''

EPSG_5181 = "epsg:5181"
EPSG_4326: str = "epsg:4326"

UTF_8 = 'utf-8'
EUC_KR = 'euc-kr'
CP_949 = 'CP949'

'''
PATH
'''

PATH_ORIGIN = "app/data/origin/"
PATH_MAP = "app/data/map/"
PATH_AFTER = "app/data/after/"
PATH_RESULT = "app/data/result/"

"""
ORIGIN_PATH
"""


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



PATH_LIFE_POPULATION_ORIGIN = PATH_ORIGIN + "life_population/"

PATH_LIFE_POPULATION_JAN = PATH_LIFE_POPULATION_ORIGIN + "jan/"
PATH_LIFE_POPULATION_FEB = PATH_LIFE_POPULATION_ORIGIN + "feb/"
PATH_LIFE_POPULATION_MAR = PATH_LIFE_POPULATION_ORIGIN + "mar/"
PATH_LIFE_POPULATION_APR = PATH_LIFE_POPULATION_ORIGIN + "apr/"
PATH_LIFE_POPULATION_MAY = PATH_LIFE_POPULATION_ORIGIN + "may/"
PATH_LIFE_POPULATION_JUN = PATH_LIFE_POPULATION_ORIGIN + "jun/"
PATH_LIFE_POPULATION_JUL = PATH_LIFE_POPULATION_ORIGIN + "jul/"
PATH_LIFE_POPULATION_AUG = PATH_LIFE_POPULATION_ORIGIN + "aug/"
PATH_LIFE_POPULATION_SEP = PATH_LIFE_POPULATION_ORIGIN + "sep/"
PATH_LIFE_POPULATION_OCT = PATH_LIFE_POPULATION_ORIGIN + "oct/"
PATH_LIFE_POPULATION_NOV = PATH_LIFE_POPULATION_ORIGIN + "nov/"
PATH_LIFE_POPULATION_DEC = PATH_LIFE_POPULATION_ORIGIN + "dec/"

'''
MAP_PATH
'''

PATH_격자_MAP = PATH_MAP + "격자.geojson"

PATH_격자_집계구_MAP = PATH_MAP + "grid_area.csv"
PATH_격자_한강_MAP = PATH_MAP + "grid_hangang.csv"
PATH_격자_관광지_MAP = PATH_MAP + "grid_tourist.csv"
PATH_격자_지하철_MAP = PATH_MAP + "grid_subway.csv"

PATH_자치구_MAP = PATH_MAP + "large_map.shp"
PATH_행정동_MAP = PATH_MAP + "middle_map.shp"
PATH_집계구_MAP = PATH_MAP + "small_map.shp"

'''
AFTER_PATH
'''
PATH_112신고접수정보_AFTER = PATH_AFTER + "report/112신고접수.csv"

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

PATH_LIFE_POPULATION_AFTER = PATH_AFTER + "life_population/"
PATH_LIFE_POPULATION_TEMP_AFTER = PATH_AFTER + "life_population/month/"



'''
PATH_LIST
'''

PATH_LIST = [PATH_ORIGIN,
             PATH_MAP,
             PATH_AFTER,
             PATH_RESULT,

             PATH_LIFE_POPULATION_AFTER,
             PATH_LIFE_POPULATION_TEMP_AFTER,

             PATH_ORIGIN + "report/",
             PATH_ORIGIN + "danger_facility/",
             PATH_ORIGIN + "police_facility/",
             PATH_ORIGIN + "safety_facility/",

             PATH_AFTER + "report/",
             PATH_AFTER + "danger_facility/",
             PATH_AFTER + "safety_facility/",
             PATH_AFTER + "danger_facility/",

             PATH_ORIGIN + "life_population/",
             PATH_AFTER + "life_population/",

             PATH_LIFE_POPULATION_JAN,
             PATH_LIFE_POPULATION_FEB,
             PATH_LIFE_POPULATION_MAR,
             PATH_LIFE_POPULATION_APR,
             PATH_LIFE_POPULATION_MAY,
             PATH_LIFE_POPULATION_JUN,
             PATH_LIFE_POPULATION_JUL,
             PATH_LIFE_POPULATION_AUG,
             PATH_LIFE_POPULATION_SEP,
             PATH_LIFE_POPULATION_OCT,
             PATH_LIFE_POPULATION_NOV,
             PATH_LIFE_POPULATION_DEC
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

    PATH_격자_집계구_MAP,
    PATH_격자_관광지_MAP,
    PATH_격자_한강_MAP,
    PATH_격자_지하철_MAP,
    PATH_격자_MAP,

    PATH_자치구_MAP,
    PATH_행정동_MAP,
    PATH_집계구_MAP
]

MONTH_PATH_LIST = [
    PATH_LIFE_POPULATION_FEB,
    PATH_LIFE_POPULATION_JAN,
    PATH_LIFE_POPULATION_MAR,
    PATH_LIFE_POPULATION_APR,
    PATH_LIFE_POPULATION_MAY,
    PATH_LIFE_POPULATION_JUN,
    PATH_LIFE_POPULATION_JUL,
    PATH_LIFE_POPULATION_AUG,
    PATH_LIFE_POPULATION_SEP,
    PATH_LIFE_POPULATION_OCT,
    PATH_LIFE_POPULATION_NOV,
    PATH_LIFE_POPULATION_DEC
]
