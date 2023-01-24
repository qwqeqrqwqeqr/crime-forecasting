from datetime import date



'''
112 신고 건수 class
'''
week_day_list = ['월', '화', '수', '목', '금', '토', '일']


class Report:

    def __init__(self, data_frame):
        self.__report = data_frame
        self.__report["TIME"] = self.__report["TIME"].map(lambda x: str(x).zfill(6)[0:2])
        self.__report["weekday"] = self.__report["DAY"].map(lambda x: week_day_list[date(int(str(x)[0:4]),int(str(x)[4:6]),int(str(x)[6:8])).weekday()])
        self.__report["x"] = (self.__report["HPPN_X_SW"] +
                  self.__report["HPPN_X_NE"] +
                  self.__report["HPPN_X_NW"] +
                  self.__report["HPPN_X_SE"]) / 4
        self.__report["y"] = (self.__report["HPPN_Y_SW"] +
                  self.__report["HPPN_Y_NE"] +
                  self.__report["HPPN_Y_NW"] +
                  self.__report["HPPN_Y_SE"]) / 4


        self.__day = self.__report["DAY"]         # yyyMMdd
        self.__weekday =  self.__report["weekday"]
        self.__time = self.__report["TIME"]     # hh
        self.__evt_cl_cd = self.__report["EVT_CL_CD"]       # 신고별 종별 코드
        self.__end_cd = self.__report["END_CD"]         # 종결 코드
        self.__x = self.__report["x"]
        self.__y = self.__report["y"]



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



