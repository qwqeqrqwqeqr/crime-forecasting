import re

from app.model.report import Report
from app.utils.constants import UTF_8

if __name__ == '__main__':
    report = Report("./data_sample/report2022_novdec.csv", encoding=UTF_8)

    # print(report.__get__())
    print(report.time)
    # print(report.get_week_day())
