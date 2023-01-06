import pandas as pd

from business.preprocessing.count_point_in_polygon.count_point_in_polygon import count_point_in_polygon
from business.preprocessing.life_population.calculate_life_population_average import calculate_life_population_average
from business.preprocessing.utils.utils import convert_csv, get_center_coordinate
from business.statistics.facility_statistics.utils import grid_df_to_list, concat_grid_data
from business.statistics.facility_statistics.converter import convert_to_grid_life_population, \
    convert_to_grid_facility, convert_to_grid_report
from utils.constants import *

'''
expand_flag : 확장 여부를 결정합니다.
depth : 얼마만큼 확장할 것인지 정하는 파라미터입니다.
'''
def service(expand_flag,depth):

    # 생활인구 평균 필요시 주석해제
    calculate_life_population_average()

    df_list = [convert_to_grid_report(), convert_to_grid_life_population()]
    df_list = convert_to_grid_facility(df_list,expand_flag,depth)



    concat_df = concat_grid_data( grid_df_to_list(df_list), '격자고유번호')

