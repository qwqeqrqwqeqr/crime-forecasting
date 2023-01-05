import os

import pandas as pd

from utils.constants import *


def calculate_life_population_average():
    df_year= []
    for path in MONTH_PATH_LIST:
        df_month = []
        for item in  os.listdir(path):
            print("파일 : [",item,"] 을 처리 합니다")
            df_month.append(pd.read_csv(path + item, encoding=EUC_KR))
            df_year.append(pd.read_csv(path + item, encoding=EUC_KR))


        dfs = pd.concat(df_month)
        dfs = dfs.groupby('집계구코드').mean().reset_index()

        print(path.split('/')[-1],"평균 파일을 저장합니다.")
        dfs.to_csv(PATH_LIFE_POPULATION_AFTER + item.split('.')[0][:-2] + ".csv")


    dfs = pd.concat(df_year)
    dfs = dfs.groupby('집계구코드').mean().reset_index()
    print("전체 평균 파일을 저장합니다.")
    dfs.to_csv(PATH_LIFE_POPULATION_AFTER + item.split('.')[0][:-4] + ".csv")


