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

input_path, output_path : 읽기 경로, 저장 경로
key1,key2,key3,key4: center coordinate 를 도출해 낼 4개 좌표 (x,y 합쳐 총 8개)
'''
def get_center_coordinate(df,key_x1,key_x2,key_x3,key_x4,key_y1,key_y2,key_y3,key_y4):
    df['x'] = (df[key_x1] + df[key_x2] + df[key_x3] + df[key_x4]) / 4
    df['y'] = (df[key_y1] + df[key_y2] + df[key_y3] + df[key_y4]) / 4
    return df[['x','y']]