import pandas as pd



def concat_grid_life_population(grid_area_map,life_population):

    # 집계구 별 격자랑 매핑
    grid_time_life_population_map = pd.merge(grid_area_map, life_population, left_on='TOT_REG_CD',
                                             right_on='집계구코드', how='inner')

    grid_time_life_population_map['count'] = grid_time_life_population_map['총생활인구수'] / grid_time_life_population_map[
        'duplicate']

    return grid_time_life_population_map[['격자고유번호', 'count']]


def calculate_life_population_average(life_population):
    return life_population.groupby('집계구코드').mean().reset_index()