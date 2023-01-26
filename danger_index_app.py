import pandas as pd

from app.utils.constants import *

'''
위험지수는 한 달 단위로 계산 됩니다.
122 신고 데이터 :  (현재 2021년 )
생활인구 데이터 포멧 :  (현재 : 2021년 데이터 총 365개)
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

    init()  # 초기 검사

    from app.model.grid_map import GridMap

    grid_map = GridMap(PATH_GRID_MAP)  # 100격자
    grid_area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)

    temp_life_population = []
    for item in os.listdir(LIFE_POPULATION_PATH):
        temp_life_population.append(pd.read_csv(LIFE_POPULATION_PATH + item, encoding=EUC_KR))

    from app.model.life_population import LifePopulation
    from app.business.ai.train_data.life_population.life_population_average import calculate_life_population_average
    from app.business.ai.train_data.life_population.concat_data import concat_grid_life_population

    life_population = concat_grid_life_population(grid_area_map, calculate_life_population_average(
        LifePopulation(pd.concat(temp_life_population)).life_population))

    temp_report = []
    for item in os.listdir(CRIME_REPORT_PATH):
        temp_report.append(pd.read_csv(CRIME_REPORT_PATH + item, encoding=UTF_8))

    from app.model.report import Report
    from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon

    report = count_point_in_polygon(grid_map.grid_map, '격자고유번호',
                                    Report(pd.concat(temp_report)).report,
                                    'x', 'y', EPSG_4326, False)

    from app.business.ai.train_data.facility.concat_data import concat_grid_facility

    facility = concat_grid_facility(grid_map.grid_map, 2)  # 시설별 격자 데이터 산출

    from app.business.ai.train_data.utils import grid_df_to_list, concat_grid_data
    train_data=concat_grid_data(grid_df_to_list([report, life_population, facility]),'격자고유번호')


    print(train_data)

    from app.service.danger_index.service import service
    service(train_data)

