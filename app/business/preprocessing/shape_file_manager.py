# -*- coding: utf-8 -*-

import geopandas as gpd
class ShapeFileManager:
    def __init__(self,path,encoding):
        self.path = path
        self.encoding = encoding
        self.shape = gpd.read_file(self.path, encoding=self.encoding)

    def get(self):
        return self.shape
    def save_to_csv(self,save_path):
        self.shape.to_csv(save_path)








