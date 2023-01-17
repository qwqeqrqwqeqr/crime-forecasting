from datetime import date

import geopandas as gpd
import pandas as pd


def read_shp(path,encoding):
    return gpd.read_file(path, encoding = encoding)


def convert_csv(input_path,output_path,encoding):
    df = read_shp(input_path,encoding)

    x,y = zip(*[(x, y) for x, y in zip(df['geometry'].x, df['geometry'].y)])
    df['x'] = x
    df['y'] = y
    df= df.drop_duplicates()
    df[['x','y']].to_csv(output_path,index=False)


'''
key1,key2,key3,key4: center coordinate 를 도출해 낼 4개 좌표 (x,y 합쳐 총 8개)
결과로 df를 반환함
'''
def get_center_coordinate(df,key_x1,key_x2,key_x3,key_x4,key_y1,key_y2,key_y3,key_y4):
    df['x'] = (df[key_x1] + df[key_x2] + df[key_x3] + df[key_x4]) / 4
    df['y'] = (df[key_y1] + df[key_y2] + df[key_y3] + df[key_y4]) / 4
    return df


'''
yyyyMMdd 를 기준으로 요일을 계산함
'''
def get_weekday(target):
    days = ['월', '화', '수', '목', '금', '토', '일']
    return days[date(int(target[0:4]), int(target[4:6]), int(target[6:8])).weekday()]
