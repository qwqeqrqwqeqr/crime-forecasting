import pandas as pd

from app.business.statistics.facility_statistics.converter import convert_to_grid_report, convert_to_grid_facility, \
    convert_to_grid_life_population

'''
expand_flag : 확장 여부를 결정합니다. true or false
depth : 얼마만큼 확장할 것인지 정하는 파라미터입니다. 
'''
def service(expand_flag,depth):

    # 생활인구 평균 필요시 주석해제
    # calculate_life_population_average()

    convert_to_grid_report()
    df_list = [convert_to_grid_report(), convert_to_grid_life_population()]
    df_list = convert_to_grid_facility(df_list,expand_flag,depth)



    # concat_df = concat_grid_data( grid_df_to_list(df_list), '격자고유번호')

    # print(concat_df)

