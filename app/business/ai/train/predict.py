import numpy as np
from app.business.ai.train import *


def predict(train_data_df, key_danger_index):

    train_data_df = generate_filter_class(train_data_df)        # generate filter class
    x_train_val, y_train_val = generate_train_data(train_data_df)       # generate data for train model

    model = LR_MODEL
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=10, random_state=RANDOM_STATE, shuffle=True)

    for train_index, val_index in kf.split(x_train_val):        # train model
        x_train, x_val = x_train_val.values[train_index], x_train_val.values[val_index]
        y_train, y_val = y_train_val.values[train_index], y_train_val.values[val_index]
        model.fit(x_train, y_train)

    save_model(model,key_danger_index)      # save model
    import pandas as pd
    cdf= pd.DataFrame(np.transpose(model.coef_), x_train_val.columns).reset_index(inplace=False).rename(columns={'index': 'feature'})
    cdf2 = pd.DataFrame()
    cdf3 = pd.DataFrame()

    for c in range(len(train_data_df[KEY_FILTER_CLASS].value_counts().to_dict().keys())):       # choice danger index
        for i in cdf['feature'].to_list():
            cdf2[i] = cdf.loc[cdf['feature'] == i].reset_index()[c][0] * train_data_df[i]
            cdf3[c] = cdf2.sum(axis=1)
    train_data_df[key_danger_index] = np.where(train_data_df[KEY_FILTER_CLASS] == 0, cdf3[0],
                                               np.where(train_data_df[KEY_FILTER_CLASS] == 1, cdf3[1],
                                                        np.where(train_data_df[KEY_FILTER_CLASS] == 2, cdf3[2],
                                                                 train_data_df[KEY_FILTER_CLASS])))
    train_data_df[key_danger_index] = train_data_df[key_danger_index].map(lambda  x : round(x,3))


    return train_data_df[['격자고유번호', key_danger_index]]

def save_model(model,key_danger_index):
    import joblib
    joblib.dump(model, MODEL_PATH(key_danger_index))

def generate_train_data(df):
    from sklearn.model_selection import train_test_split
    x_train_val, x_test, y_train_val, y_test = train_test_split(df.iloc[:, :-1], df[KEY_FILTER_CLASS],
                                                                test_size=0.10, random_state=42, shuffle=True)
    x_train_val = x_train_val.iloc[:, 2:]

    from sklearn.preprocessing import MinMaxScaler      # preprocessing
    scaler = MinMaxScaler()
    scaler.fit(x_train_val)
    import pandas as pd
    x_train_val = pd.DataFrame(scaler.transform(x_train_val), columns=x_train_val.columns)

    return x_train_val, y_train_val


def generate_filter_class(df):
    df.fillna(0, inplace=True)
    df['num'] = (df['112신고데이터'] + 0.0000000001) / df['생활인구']
    df.fillna(0, inplace=True)


    q1, q2, q3, q4 = np.percentile(df['num'], [25, 50, 75, 100])
    upper_fence = q3 + (1.5 * (q3 - q1))
    df[KEY_FILTER_CLASS] = np.digitize(x=df['num'], bins=[q2, upper_fence], right=True)       # generate filter class
    return df.drop(columns=['num'])
