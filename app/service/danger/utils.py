from datetime import datetime
from functools import reduce

import pandas as pd

from app.service.danger.constants import GRID_NAME_LIST


# 격자별로 데이터를 하나로 통합한다
def concat_grid_data(dfs,map_key):
    return reduce(lambda left, right: pd.merge(left, right, on=map_key), dfs)


# 시설정보 df들을 리스트 묶음으로 변환함
def grid_df_to_list(df_list):
    dfs = []
    for i in range(0, len(GRID_NAME_LIST)):
        df = df_list[i]
        df = df.rename(columns={'count': GRID_NAME_LIST[i]})
        dfs.append(df)
    return dfs