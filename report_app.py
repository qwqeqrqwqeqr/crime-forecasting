import sys

import pandas as pd
import geopandas as gpd

from app.business.preprocessing.utils.utils import get_center_coordinate
from app.utils.constants import *
from app.utils.utils import init

'''
입력 신고 데이터 포멧 : KPU_99_YYYYMMDD_C_001.csv 
argv[1] : 112 신고 데이터
EVT_CL_CD : 사건 종별 코드를 의미함
END_CD : 종결 코드를 의미
PATH_GRID_MAP : 격자 데이터
'''

CRIME_REPORT_PATH = sys.argv[1]

if __name__ == '__main__':
    # 초기 검사
    init()

    print("========== 112 신고 [유형별 발생 건수]를 산출 합니다. ==========")
    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")
    chunk_df = pd.read_csv(CRIME_REPORT_PATH, encoding=UTF_8, chunksize=5)
    for chunk in chunk_df:
        df = get_center_coordinate(chunk,
                                   'HPPN_X_SW', 'HPPN_X_NE', 'HPPN_X_NW', 'HPPN_X_SE',
                                   'HPPN_Y_SW', 'HPPN_Y_NE', 'HPPN_Y_NW', 'HPPN_Y_SE').fillna(0).astype(
            {'EVT_CL_CD': 'int', 'END_CD': 'int'})
        day_month_year_list = list(set(df['DAY'].values.tolist()))
        for day_month_year in day_month_year_list:
            from app.service.report.service import service
            service(grid_map, df.loc[df['DAY'] == day_month_year])


