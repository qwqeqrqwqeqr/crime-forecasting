from app.business.preprocessing.utils.utils import read_shp
from app.utils.constants import *

if __name__ == '__main__':
    shp=read_shp("./app/data/map/large_map.shp",CP_949)

    shp.to_csv("./large_map.csv")
    print(shp)

