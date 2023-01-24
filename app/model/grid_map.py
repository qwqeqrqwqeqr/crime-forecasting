import geopandas as gpd

'''
격자 class
'''
class GridMap:
    def __init__(self, path):
        self.__grid_map = gpd.read_file(path, driver="GeoJSON")
        self.__grid_number = self.__grid_map["격자고유번호"].map(lambda x: x[-6:])
    @property
    def grid_number(self):
        return self.__grid_number

    @property
    def grid_map(self):
        return self.__grid_map