# -*- coding: utf-8 -*-




def concat_grid_data(dfs,map_key):
    from functools import reduce
    import pandas as pd

    return reduce(lambda left, right: pd.merge(left, right, on=map_key), dfs)


def grid_df_to_list(df_list,key,name_list):
    dfs = []

    for i in range(0, len(name_list)):
        df = df_list[i]
        df = df.rename(columns={key: name_list[i]})
        dfs.append(df)
    return dfs


