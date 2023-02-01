# -*- coding: utf-8 -*-


class GridMap:      # Grid DataFrame Class
    def __init__(self, data_frame):

        self.__grid_map = data_frame
        self.__grid_map["grid_number"] = self.__grid_map["격자고유번호"].map(lambda x: x[-6:])
        self.__grid_number = self.__grid_map["grid_number"]
    @property
    def grid_number(self):
        return self.__grid_number

    @property
    def grid_map(self):
        return self.__grid_map