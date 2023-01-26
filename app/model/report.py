from datetime import date


class Report:  # 112 신고 건수 DaraFrame Class

    def __init__(self, data_frame):
        self.__week_day_list = ['월', '화', '수', '목', '금', '토', '일']

        self.__report = data_frame
        self.__report["hour"] = self.__report["TIME"].map(lambda x: str(x).replace(' ','').zfill(6)[0:2])
        self.__report["DAY"] = self.__report["DAY"].map(lambda x: str(x))  # yyyyMMdd

        self.__report["weekday"] = self.__report["DAY"].map(
            lambda x: self.__week_day_list[date(int(str(x)[0:4]), int(str(x)[4:6]), int(str(x)[6:8])).weekday()])
        self.__report["month"] = self.__report["DAY"].map(lambda x: str(x)[4:6])
        self.__report["x"] = (self.__report["HPPN_X_SW"] +
                              self.__report["HPPN_X_NE"] +
                              self.__report["HPPN_X_NW"] +
                              self.__report["HPPN_X_SE"]) / 4
        self.__report["y"] = (self.__report["HPPN_Y_SW"] +
                              self.__report["HPPN_Y_NE"] +
                              self.__report["HPPN_Y_NW"] +
                              self.__report["HPPN_Y_SE"]) / 4
        self.__report["evt_cl_cd"] = self.__report["EVT_CL_CD"].map(lambda x: str(x).split('.')[0])
        self.__report["end_cd"] = self.__report["END_CD"].map(lambda x: str(int(str(x).replace('{', '0').replace('nan','0').split('.')[0])))
        self.__day = self.__report["DAY"]  # yyyyMMdd
        self.__month = self.__report["month"]  # MM
        self.__weekday = self.__report["weekday"]  # 월화수목금토일
        self.__time = self.__report["TIME"]  # hhmmss
        self.__hour = self.__report["hour"]  # hh
        self.__evt_cl_cd = self.__report["evt_cl_cd"]  # 신고별 종별 코드
        self.__end_cd = self.__report["end_cd"]  # 종결 코드
        self.__x = self.__report["x"]
        self.__y = self.__report["y"]

    def get_day_list(self): return list(set(self.__day.tolist()))

    def get_hour_list(self): return list(set(self.__hour.tolist()))

    def get_month_list(self): return list(set(self.__month.tolist()))

    def get_report_filtered_day(self, day_month_year): return Report(self.__report.loc[self.__day == day_month_year])

    def get_report_filtered_hour(self, hour): return Report(self.__report.loc[self.__hour == hour])

    @property
    def report(self):
        return self.__report

    @property
    def day(self):
        return self.__day

    @property
    def weekday(self):
        return self.__weekday

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
