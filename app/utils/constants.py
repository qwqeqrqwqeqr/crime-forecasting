
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


PATH_NY_ORIGIN = PATH_ORIGIN + "danger_facility/서울시노래연습장업인허가정보.csv"
PATH_DJ_ORIGIN = PATH_ORIGIN + "danger_facility/서울시단란주점영업인허가정보.csv"
PATH_MJ_ORIGIN = PATH_ORIGIN + "danger_facility/서울시목욕장업인허가정보.csv"
PATH_SB_ORIGIN = PATH_ORIGIN + "danger_facility/서울시숙박업인허가정보.csv"
PATH_YH_ORIGIN = PATH_ORIGIN + "danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_ICG_ORIGIN = PATH_ORIGIN + "danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"

PATH_POLICE_OFFICE_ORIGIN = PATH_ORIGIN + "police_facility/경찰서.csv"
PATH_SAFETY_CENTER_ORIGIN = PATH_ORIGIN + "police_facility/치안센터.csv"
PATH_POICE_STATION_ORIGIN = PATH_ORIGIN + "police_facility/파출소지구대.csv"

PATH_CCTV_ORIGIN = PATH_ORIGIN + "safety_facility/서울시_CCTV_설치현황.csv"
PATH_SMART_SECURITY_LIGHT_ORIGIN = PATH_ORIGIN + "safety_facility/스마트보안등.csv"
PATH_DELIVERY_BOX_ORIGIN = PATH_ORIGIN + "safety_facility/여성안심택배함.csv"
PATH_SAFETY_HOUSE_ORIGIN = PATH_ORIGIN + "safety_facility/여성안심지킴이집.csv"
PATH_SAFETY_FACILITY_ORIGIN = PATH_ORIGIN + "safety_facility/아동안전지킴이시설물.csv"
PATH_CONVENIENCE_STORE_ORIGIN = PATH_ORIGIN + "safety_facility/편의점.csv"



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

PATH_GRID_MAP = PATH_MAP + "grid.geojson"

PATH_GRID_AREA_MAP = PATH_MAP + "grid_area.csv"
PATH_GRID_HANGANG_MAP = PATH_MAP + "grid_hangang.csv"
PATH_GRID_TOURIST_MAP = PATH_MAP + "grid_tourist.csv"
PATH_GRID_SUBWAY_MAP = PATH_MAP + "grid_subway.csv"

PATH_LARGE_MAP = PATH_MAP + "large_map.csv"
PATH_MIDDLE_MAP = PATH_MAP + "middle_map.csv"
PATH_SMALL_MAP = PATH_MAP + "small_map.csv"

'''
AFTER_PATH
'''

PATH_POLICE_OFFICE_AFTER = PATH_AFTER + "police_facility/경찰서.csv"
PATH_SAFETY_CENTER_AFTER = PATH_AFTER + "police_facility/치안센터.csv"
PATH_POLICE_STATION_AFTER = PATH_AFTER + "police_facility/파출소지구대.csv"

PATH_CCTV_AFTER = PATH_AFTER + "safety_facility/서울시_CCTV_설치현황.csv"
PATH_SMART_SECURITY_LIGHT_AFTER = PATH_AFTER + "safety_facility/스마트보안등.csv"
PATH_DELIVERY_BOX_AFTER = PATH_AFTER + "safety_facility/여성안심택배함.csv"
PATH_SAFETY_HOUSE_AFTER = PATH_AFTER + "safety_facility/여성안심지킴이집.csv"

PATH_SAFETY_FACILITY_AFTER = PATH_AFTER + "safety_facility/아동안전지킴이시설물.csv"
PATH_CONVENIENCE_STORE_AFTER = PATH_AFTER + "safety_facility/편의점.csv"

PATH_NY_AFTER = PATH_AFTER + "danger_facility/서울시노래연습장업인허가정보.csv"
PATH_DJ_AFTER = PATH_AFTER + "danger_facility/서울시단란주점영업인허가정보.csv"
PATH_MJ_AFTER = PATH_AFTER + "danger_facility/서울시목욕장업인허가정보.csv"
PATH_SB_AFTER = PATH_AFTER + "danger_facility/서울시숙박업인허가정보.csv"
PATH_YH_AFTER = PATH_AFTER + "danger_facility/서울시유흥주점영업인허가정보.csv"
PATH_ICG_AFTER = PATH_AFTER + "danger_facility/서울시인터넷컴퓨터게임시설제공업인허가정보.csv"

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

    PATH_NY_ORIGIN,
    PATH_DJ_ORIGIN,
    PATH_MJ_ORIGIN,
    PATH_SB_ORIGIN,
    PATH_YH_ORIGIN,
    PATH_ICG_ORIGIN,

    PATH_POLICE_OFFICE_ORIGIN,
    PATH_SAFETY_CENTER_ORIGIN,
    PATH_POICE_STATION_ORIGIN,

    PATH_CCTV_ORIGIN,
    PATH_SMART_SECURITY_LIGHT_ORIGIN,
    PATH_DELIVERY_BOX_ORIGIN,
    PATH_SAFETY_HOUSE_ORIGIN,

    PATH_GRID_AREA_MAP,
    PATH_GRID_TOURIST_MAP,
    PATH_GRID_HANGANG_MAP,
    PATH_GRID_SUBWAY_MAP,
    PATH_GRID_MAP,

    PATH_LARGE_MAP,
    PATH_MIDDLE_MAP,
    PATH_SMALL_MAP
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
