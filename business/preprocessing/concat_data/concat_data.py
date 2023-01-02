from functools import reduce

import pandas as pd

from utils.constants import *


def concat_data(dfs):
    concat_result = reduce(lambda left, right: pd.merge(left, right, on='격자고유번호'), dfs)
    concat_result.to_csv(PATH_시설별신고건수_RESULT,index=False)

