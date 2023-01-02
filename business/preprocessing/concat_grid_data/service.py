import pandas as pd

from business.preprocessing.concat_grid_data.concat_grid_data import grid_df_to_list, concat_grid_data


#
def service():
    dfs= grid_df_to_list([])
    concat_grid_data(dfs,'격자고유번호')
