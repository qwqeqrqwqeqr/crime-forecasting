import numpy as np

# for train & test data with spatial regression
def spatial_regression(train_data_df):
    pass


def geographically_weighted_regression(df):
    x,y,coordinate =generate_train_data(df)
    #start modelling
    from mgwr.gwr import GWR
    from mgwr.sel_bw import Sel_BW

    mgwr_selector = Sel_BW(coordinate, y, x)
    mgwr_bw = mgwr_selector.search() #save result of bandwith
    gwr_results = GWR(coordinate, y, x, mgwr_bw).fit()

    gwr_results.summary() #print model summary result

    # Add GWR parameters to GeoDataframe
    df['gwr_x0'] = gwr_results.params[:,0]
    df['gwr_x1'] = gwr_results.params[:,1]
    df['gwr_x2'] = gwr_results.params[:,2]
    df['gwr_x3'] = gwr_results.params[:,3]
    df['gwr_x4'] = gwr_results.params[:,4]
    df['gwr_x5'] = gwr_results.params[:,5]
    df['gwr_x6'] = gwr_results.params[:,6]
    df['gwr_x7'] = gwr_results.params[:,7]
    df['gwr_x8'] = gwr_results.params[:,8]
    df['gwr_x9'] = gwr_results.params[:,9]
    df['gwr_x10'] = gwr_results.params[:,10]
    df['gwr_x11'] = gwr_results.params[:,11]
    df['gwr_x12'] = gwr_results.params[:,12]
    df['gwr_x13'] = gwr_results.params[:,13]
    df['gwr_x14'] = gwr_results.params[:,14]
    df['gwr_x15'] = gwr_results.params[:,15]
    df['gwr_x16'] = gwr_results.params[:,16]

    return df


def save_model(model):
    import pickle
    pickle.dump(model, open('gwr_model.pkl', 'wb'))  # save model as pickle


def generate_train_data(df):
    from shapely.wkt import loads
    df.geometry = df['geometry'].apply(loads)
    train_df = df.iloc[:, 1:18]
    train_df["x"] = df.centroid.x
    train_df["y"] = df.centroid.y
    train_df = train_df.astype(float)
    y = train_df['112신고데이터'].values.reshape((-1, 1))
    x = train_df[['생활인구', 'CCTV', '보안등', '편의점', '여성안심지킴이집', '여성안심택배함', '아동안전지킴이시설물',
                  '인터넷컴퓨터게임시설', '노래연습장', '단란주점', '유흥주점', '목욕장업', '숙박업', '지구대/파출소', '치안센터', '접수경찰서']].values
    x = x + 0.00001 * np.random.rand(61648, 16)

    return x,y,list(zip(train_df['x'], train_df['y']))



