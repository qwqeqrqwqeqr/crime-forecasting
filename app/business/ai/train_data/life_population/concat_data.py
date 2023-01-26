import pandas as pd

from app.utils.constants import PATH_GRID_AREA_MAP, UTF_8


def concat_grid_life_population(life_population):
    print("격자 별 생활 인구를 산출 합니다.")
    area_map = pd.read_csv(PATH_GRID_AREA_MAP, encoding=UTF_8)

    # 집계구 별 격자랑 매핑
    grid_time_life_population_map = pd.merge(area_map, life_population, left_on='TOT_REG_CD',
                                             right_on='집계구코드', how='inner')

    grid_time_life_population_map['count'] = grid_time_life_population_map['총생활인구수'] / grid_time_life_population_map[
        'duplicate']
    return grid_time_life_population_map[['격자고유번호', 'count']]
