from business.preprocessing.expand_data.expand_data import expand_data
from utils.constants import *

'''
depth : 확장할 격자 범위 
overwrite : 덮어쓰기 여부  (덮어 쓸 경우, 확장된 시설 기준으로 분석을 시작할 수 있다.)
'''


def service(depth, overwrite):
    print("========== 시설 개수를 확장합니다. ==========")
    expand_data(depth, PATH_여성안심지킴이집_AFTER, PATH_여성안심지킴이집_AFTER, UTF_8)
    expand_data(depth, PATH_여성안심택배함_AFTER, PATH_여성안심택배함_AFTER, UTF_8)
    expand_data(depth, PATH_아동안전지킴이시설물_AFTER, PATH_아동안전지킴이시설물_AFTER, UTF_8)
    expand_data(depth, PATH_편의점_AFTER, PATH_편의점_AFTER, UTF_8)

    expand_data(depth, PATH_경찰서_AFTER, PATH_경찰서_AFTER, UTF_8)
    expand_data(depth, PATH_치안센터_AFTER, PATH_치안센터_AFTER, UTF_8)
    expand_data(depth, PATH_파출소지구대_AFTER, PATH_파출소지구대_AFTER, UTF_8)
