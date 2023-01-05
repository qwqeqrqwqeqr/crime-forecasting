import os

import pandas as pd

from utils.constants import *


def calculate_life_population_average():
    print("생활 인구의 평균을 계산 합니다.")
    for path in MONTH_PATH_LIST:
        get_average(path, EUC_KR).to_csv(
            PATH_LIFE_POPULATION_TEMP_AFTER + os.listdir(path)[0].split('.')[0][:-2] + ".csv")
        print(path.split('/')[-1], "평균 파일을 저장 하였습니다.")

    get_average(PATH_LIFE_POPULATION_TEMP_AFTER, UTF_8).to_csv(
        PATH_LIFE_POPULATION_AFTER + os.listdir(PATH_LIFE_POPULATION_TEMP_AFTER)[0].split('.')[0][:-2] + ".csv")
    print("전체 평균 파일을 저장 하였습니다.")


def get_average(path, encoding):
    dfs = []
    for item in os.listdir(path):
        print("파일 : [", item, "] 을 처리 합니다")
        dfs.append(pd.read_csv(path + item, encoding=encoding))

    dfs = pd.concat(dfs)
    return dfs.groupby('집계구코드').mean().reset_index()
