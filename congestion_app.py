
import pandas as pd

from app.utils.constants import *


'''
혼잡도는 1달 단위로 계산함
122 신고 데이터 :  1달 신고 데이터
생활인구 데이터 포멧 :  1달 단위
PATH_GRID_AREA_MAP : 집계구 격자 데이터
PATH_GRID_MAP : 격자 데이터
'''

import os
import sys
CRIME_REPORT_PATH = sys.argv[1]
LIFE_POPULATION_PATH = sys.argv[2]

if __name__ == '__main__':

    import warnings
    warnings.filterwarnings(action='ignore')

    from app.utils.utils import init
    init()      # 초기 검사


    temp_life_population= []
    for item in os.listdir(LIFE_POPULATION_PATH):
         temp_life_population.append(pd.read_csv(LIFE_POPULATION_PATH + item, encoding=EUC_KR))

    from app.model.life_population import LifePopulation
    life_population = LifePopulation(pd.concat(temp_life_population))       # 생활인구 통합


    temp_report=[]
    for item in os.listdir(CRIME_REPORT_PATH):
        temp_report.append(pd.read_csv(CRIME_REPORT_PATH + item,  encoding=UTF_8))

    from app.model.report import Report
    report = Report(pd.concat(temp_report))         # 112 신고 건수 통합

    from app.model.grid_map import GridMap
    grid_map = GridMap(PATH_GRID_MAP)       # 100격자


    grid_area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)
    grid_congestion_map = pd.read_csv(PATH_GRID_CONGESTION_MAP, encoding=UTF_8)


    from app.service.congestion.service import service
    service(grid_area_map,grid_congestion_map,grid_map,life_population,report)





