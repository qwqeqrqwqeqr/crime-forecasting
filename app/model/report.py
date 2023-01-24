from datetime import date

import pandas as pd

'''
112 신고 건수 DF class
'''


# TODO 수정 진행중

class Report:
    RECV_NO = "RECV_NO"
    DAY = "DAY"  # yyyyMMdd
    TIME = "TIME"  # hhmm
    EVT_CL_CD = "EVT_CL_CD"  # 신고별 종별 코드
    RECV_EMG_CD = "RECV_EMG_CD"
    RPTER_SEX = "RPTER_SEX"
    TRC_TYPE = "TRC_TYPE"
    HPPN_X_SW = "HPPN_X_SW"
    HPPN_X_NE = "HPPN_X_NE"
    HPPN_X_NW = "HPPN_X_NW"
    HPPN_X_SE = "HPPN_X_SE"
    HPPN_Y_SW = "HPPN_Y_SW"
    HPPN_Y_NE = "HPPN_Y_NE"
    HPPN_Y_NW = "HPPN_Y_NW"
    HPPN_Y_SE = "HPPN_Y_SE"
    END_CD = "END_CD"  # 종결 코드

    def __init__(self, path, encoding):
        self.__report = pd.read_csv(path, encoding=encoding)

        self.__day = self.__report["DAY"]         # yyyMMdd
        self.__time = self.__report["TIME"].apply(self.__fill_zero__)       #
        self.__evt_cl_cd = self.__report["EVT_CL_CD"]
        self.__end_cd = self.__report["END_CD"]
        self.__x = (self.__report["HPPN_X_SW"] +
                  self.__report["HPPN_X_NE"] +
                  self.__report["HPPN_X_NW"] +
                  self.__report["HPPN_X_SE"]) / 4

        self.__y = (self.__report["HPPN_Y_SW"] +
                  self.__report["HPPN_Y_NE"] +
                  self.__report["HPPN_Y_NW"] +
                  self.__report["HPPN_Y_SE"]) / 4


    def __fill_zero__(self, values):
        return (str(values).zfill(6))[0:2]

    def date_report(self,day_month_year):
        return self.__report[self.__day==day_month_year]
    @property
    def report(self):
        return self.__report

    @property
    def day(self):
        return self.__day
    @property
    def time(self):
        return self.__time

    @property
    def evt_cl_cd(self):
        return self.__evt_cl_cd

    @property
    def end_cd(self):
        return self.__end_cd

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def get_week_day(self):
        days = ['월', '화', '수', '목', '금', '토', '일']
        return days[date(int(self.__day[0:4]), int(self.__day[4:6]), int(self.__day[6:8])).weekday()]