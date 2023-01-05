import os
from datetime import datetime

import pandas as pd

from utils.constants import *

now = datetime.now()


# name = item.split('.')[-8:]
def service():
    area_map = pd.read_csv(PATH_격자_집계구_MAP, encoding=UTF_8)

    report_df = pd.read_csv(PATH_112신고접수정보_ORIGIN)
    report_df = report_df.astype({'TIME':'str'})
    report_df['NEW_TIME'] = report_df['TIME'].apply(fill_zero)

    # report_df = report_df.groupby("NEW_TIME")['RECV_NO'].count()


    print(area_map)
    for path in MONTH_PATH_LIST:
        for item in os.listdir(path):
            statistics_df = pd.DataFrame([], columns=[])

            print("파일 : [", item, "] 의 생활인구를 계산 합니다")
            life_population_df = pd.read_csv(path + item, encoding=EUC_KR)

            for t in range(0, 24):
                #시간대 별로 생활인구를 분할한다.
                time_condition = life_population_df['시간대구분'] == t
                time_life_population_df=life_population_df[time_condition]

                grid_time_life_population_map = pd.merge(area_map, time_life_population_df, left_on='TOT_REG_CD',
                                                    right_on='집계구코드', how='inner')

                statistics_df['생활인구'] = grid_time_life_population_map['총생활인구수']/grid_time_life_population_map['duplicate']
                statistics_df['기준일'] = item.split('.')[0][-8:]

                # (report_df.DAY == item.split('.')[0][-8:]) &



                a = report_df[report_df['NEW_TIME'] == str(t).zfill(2)]

                print(a.head())


            # print(grid_life_population_map)
            #
            #
            # grid_life_population_map.to_csv(PATH_혼잡도_RESULT+"congestion.csv")

            # ['기준일ID']['duplicate']['시간대구분']['집계구코드']['총생활인구수']


    # print(now.date())
    # df = pd.read_csv(PATH_112신고접수정보_ORIGIN)
    # df = df.astype({'TIME':'str'}

    # df = df.groupby("NEW_TIME")['RECV_NO'].count()

    # print(df)
    #
    #
    # print(statistics_df)


def fill_zero(values):
    return values.zfill(6)[0:2]
