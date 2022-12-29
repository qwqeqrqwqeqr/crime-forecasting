import geopandas as gpd


def read_shp(path,encoding):
    return gpd.read_file(path, encoding = encoding)


def convert_csv(input_path,output_path,encoding):
    df = read_shp(input_path,encoding)

    x,y = zip(*[(x, y) for x, y in zip(df['geometry'].x, df['geometry'].y)])
    df['x'] = x
    df['y'] = y
    df= df.drop_duplicates()
    df[['x','y']].to_csv(output_path,index=False)

