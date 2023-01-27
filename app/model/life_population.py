# -*- coding: utf-8 -*-

from datetime import date

class LifePopulation:  # 생활인구 DaraFrame Class

    def __init__(self, data_frame):
        self.__week_day_list = ['월', '화', '수', '목', '금', '토', '일']

        self.__life_population = data_frame.dropna(subset=['?"기준일ID"'])
        self.__life_population["hour"] = self.__life_population["시간대구분"].map(lambda x: str(x).zfill(2))
        self.__life_population['?"기준일ID"'] = self.__life_population['?"기준일ID"'].map(lambda x: str(int(x)))

        self.__life_population["weekday"] = self.__life_population['?"기준일ID"'].map(
            lambda x: self.__week_day_list[date(int(str(x)[0:4]), int(str(x)[4:6]), int(str(x)[6:8])).weekday()])

        self.__time = self.__life_population["시간대구분"]
        self.__hour = self.__life_population["hour"]
        self.__day = self.__life_population['?"기준일ID"']
        self.__weekday = self.__life_population["weekday"]

        self.__total_population = self.__life_population["총생활인구수"]
        self.__area_code = self.__life_population["집계구코드"]

    def get_day_list(self): return list(set(self.__day.tolist()))

    def get_hour_list(self): return list(set(self.__hour.tolist()))

    def get_life_population_filtered_day(self, day_month_year): return LifePopulation(
        self.__life_population.loc[self.__day == day_month_year])

    def get_life_population_filtered_hour(self, hour): return LifePopulation(
        self.__life_population.loc[self.__hour == hour])

    @property
    def life_population(self):
        return self.__life_population

    @property
    def time(self):
        return self.__time

    @property
    def day(self):
        return self.__day

    @property
    def weekday(self):
        return self.__weekday

    @property
    def total_population(self):
        return self.__total_population

    @property
    def area_code(self):
        return self.__area_code
