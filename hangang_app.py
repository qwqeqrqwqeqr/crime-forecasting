import sys

import pandas as pd

from app.business.preprocessing.utils.utils import get_center_coordinate, get_weekday
from app.utils.constants import *
from app.utils.utils import init
from app.utils.code_book import *

'''
입력 신고데이터 포멧 : KPU_99_YYYYMMDD_C_001.csv 
argv[1] : 112 신고 데이터

'''

CRIME_REPORT_PATH = sys.argv[1]

if __name__ == '__main__':
    # 초기 검사
    init()

    area_map = pd.read_csv(PATH_격자_한강_MAP, encoding=UTF_8)

    df = get_center_coordinate(pd.read_csv(CRIME_REPORT_PATH, encoding=UTF_8),
                          'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                          'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE')


    year = str(df['DAY'].iloc[0])[0:4]
    month = str(df['DAY'].iloc[0])[4:6]
    day_month_year = str(df['DAY'].iloc[0])
    weekday = get_weekday(str(df['DAY'].iloc[0]))


    print(year)
    print(month)
    print(day_month_year)
    print(weekday)

    print(df)