import numpy as np

# generate danger index with spatial regression
def spatial_regression(train_data_df):

    gwr_df=geographically_weighted_regression(train_data_df)
    danger_index_df=generate_danger_index(gwr_df)

    return danger_index_df


def geographically_weighted_regression(df):
    x,y,coordinate =generate_train_data(df)

    from mgwr.gwr import GWR
    from mgwr.sel_bw import Sel_BW

    mgwr_selector = Sel_BW(coordinate, y, x)
    model = GWR(coordinate, y, x, mgwr_selector.search()).fit()

    # add GWR parameters to GeoDataframe
    df['gwr_x0'] = model.params[:,0]
    df['gwr_x1'] = model.params[:,1]
    df['gwr_x2'] = model.params[:,2]
    df['gwr_x3'] = model.params[:,3]
    df['gwr_x4'] = model.params[:,4]
    df['gwr_x5'] = model.params[:,5]
    df['gwr_x6'] = model.params[:,6]
    df['gwr_x7'] = model.params[:,7]
    df['gwr_x8'] = model.params[:,8]
    df['gwr_x9'] = model.params[:,9]
    df['gwr_x10'] = model.params[:,10]
    df['gwr_x11'] = model.params[:,11]
    df['gwr_x12'] = model.params[:,12]
    df['gwr_x13'] = model.params[:,13]
    df['gwr_x14'] = model.params[:,14]
    df['gwr_x15'] = model.params[:,15]
    df['gwr_x16'] = model.params[:,16]

    report_model(model)      # report model summary
    return df

def report_model(model):
    from log import logger
    logger.info(f"[report] : %s" %model.summary())

def generate_danger_index(df):
    danger_index_df = df[['격자고유번호', '112신고데이터']]

    # count danger index of each feature
    danger_index_df['생활인구'] = df['생활인구'] * df['gwr_x1']
    danger_index_df['CCTV'] = df['CCTV'] * df['gwr_x2']
    danger_index_df['보안등'] = df['보안등'] * df['gwr_x3']
    danger_index_df['편의점'] = df['편의점'] * df['gwr_x4']
    danger_index_df['여성안심지킴이집'] = df['여성안심지킴이집'] * df['gwr_x5']
    danger_index_df['여성안심택배함'] = df['여성안심택배함'] * df['gwr_x6']
    danger_index_df['아동안전지킴이시설물'] = df['아동안전지킴이시설물'] * df['gwr_x7']
    danger_index_df['인터넷컴퓨터게임시설'] = df['인터넷컴퓨터게임시설'] * df['gwr_x8']
    danger_index_df['노래연습장'] = df['노래연습장'] * df['gwr_x9']
    danger_index_df['단란주점'] = df['단란주점'] * df['gwr_x10']
    danger_index_df['유흥주점'] = df['유흥주점'] * df['gwr_x11']
    danger_index_df['목욕장업'] = df['목욕장업'] * df['gwr_x12']
    danger_index_df['숙박업'] = df['숙박업'] * df['gwr_x13']
    danger_index_df['지구대/파출소'] = df['지구대/파출소'] * df['gwr_x14']
    danger_index_df['치안센터'] = df['치안센터'] * df['gwr_x15']
    danger_index_df['접수경찰서'] = df['접수경찰서'] * df['gwr_x16']


    danger_index_df['위험지수'] = danger_index_df.iloc[:, -16:].sum(axis=1)       # sum all danger index of each feature

    # categorize danger index
    q1, q2, q3, q4 = np.percentile(danger_index_df['위험지수'], [25, 50, 75, 100])
    upper_fence = q3 + (1.5 * (q3 - q1))
    danger_index_df['위험지수클래스분류'] = np.digitize(x=danger_index_df['위험지수'], bins=[q2, upper_fence], right=True)

    return danger_index_df

def save_model(model):
    import pickle
    from app.business.ai.danger_index import SR_DANGER_INDEX_MODEL_PATH
    pickle.dump(model, open(SR_DANGER_INDEX_MODEL_PATH, 'wb'))  # save model as pickle


def generate_train_data(df):

    train_df = df.iloc[:, 1:18]
    train_df["x"] = df.centroid.x
    train_df["y"] = df.centroid.y
    train_df = train_df.astype(float)
    y = train_df['112신고데이터'].values.reshape((-1, 1))
    x = train_df[['생활인구', 'CCTV', '보안등', '편의점', '여성안심지킴이집', '여성안심택배함', '아동안전지킴이시설물',
                  '인터넷컴퓨터게임시설', '노래연습장', '단란주점', '유흥주점', '목욕장업', '숙박업', '지구대/파출소', '치안센터', '접수경찰서']].values
    x = x + 0.00001 * np.random.rand(61648, 16)

    return x,y,list(zip(train_df['x'], train_df['y']))



