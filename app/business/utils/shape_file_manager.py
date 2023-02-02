# -*- coding: utf-8 -*-

class ShapeFileManager:         # read and save shape file
    def __init__(self,path,encoding):
        self.path = path
        self.encoding = encoding
        import geopandas as gpd
        self.shape = gpd.read_file(self.path, encoding=self.encoding)

    def get(self):
        return self.shape
    def save_to_csv(self,save_path):
        self.shape.to_csv(save_path)








