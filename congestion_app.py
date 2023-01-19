import sys

import pandas as pd


from app.business.preprocessing.utils.utils import get_center_coordinate
from app.utils.constants import *
import geopandas as gpd
from app.utils.utils import init


'''
122 신고 데이터 :  (현재 2021년 )
생활인구 데이터 포멧 :  (현재 : 2021년 데이터 총 365개)
PATH_격자_집계구_MAP : 집계구 격자 데이터
PATH_격자_MAP : 격자 데이터
'''


if __name__ == '__main__':
    # 초기 검사
    init()

    area_map = pd.read_csv(PATH_격자_집계구_MAP, encoding=UTF_8)
    grid_map = gpd.read_file(PATH_격자_MAP, driver="GeoJSON")
    df = get_center_coordinate(pd.read_csv(PATH_112신고접수정보_ORIGIN, encoding=UTF_8),
                               'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                               'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')

    from app.service.congestion.service import service
    service(area_map,grid_map,df)



