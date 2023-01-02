import pandas as pd
from functools import reduce
import pandas as pd

def concat_data(dfs):
    df_merge = reduce(lambda left, right: pd.merge(left, right, on='name'), dfs)
    
