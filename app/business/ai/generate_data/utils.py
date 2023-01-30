# -*- coding: utf-8 -*-




def concat_grid_data(dfs,map_key):
    from functools import reduce
    import pandas as pd

    return reduce(lambda left, right: pd.merge(left, right, on=map_key), dfs)


def grid_df_to_list(df_list):
    dfs = []

    from app.business.ai.generate_data import GRID_NAME_LIST
    for i in range(0, len(GRID_NAME_LIST)):
        df = df_list[i]
        df = df.rename(columns={'count': GRID_NAME_LIST[i]})
        dfs.append(df)
    return dfs


