import sys

import pandas as pd
import geopandas as gpd

from app.business.preprocessing.utils.utils import get_center_coordinate
from app.model.report import Report
from app.utils.constants import *
from app.utils.utils import init

'''
입력 신고 데이터 포멧 : KPU_99_YYYYMMDD_C_001.csv 
argv[1] : 112 신고 데이터
EVT_CL_CD : 사건 종별 코드를 의미함
END_CD : 종결 코드를 의미
PATH_GRID_SUBWAY_MAP : 지하철 격자 데이터
PATH_지하철_MAP : 격자 데이터
'''

CRIME_REPORT_PATH = sys.argv[1]

if __name__ == '__main__':
    # 초기 검사
    init()

    print("========== 112신고 빈도데이터 - [지하철 경찰대]를 산출 합니다. ==========")
    area_map = pd.read_csv(PATH_GRID_SUBWAY_MAP, encoding=UTF_8)
    grid_map = gpd.read_file(PATH_GRID_MAP, driver="GeoJSON")

    report = Report(CRIME_REPORT_PATH, UTF_8)
    day_month_year_list = list(set(report.day.tolist()))
    for day_month_year in day_month_year_list:
        from app.service.subway.service import service
        service(area_map, grid_map, report.date_report(day_month_year))
