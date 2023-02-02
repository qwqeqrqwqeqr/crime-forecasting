# -*- coding: utf-8 -*-

def concat_grid_data(dfs,map_key):      # reduce dataframe list on key
    from functools import reduce
    import pandas as pd
    df = reduce(lambda left, right: pd.merge(left, right, on=map_key), dfs)
    return df

def rename_dataframe(df_list,key,name_list):
    dfs = []
    for i in range(0, len(name_list)):
        df = df_list[i]
        df = df.rename(columns={key: name_list[i]})
        dfs.append(df)
    return dfs


