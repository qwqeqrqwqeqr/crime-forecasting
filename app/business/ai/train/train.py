import numpy as np
import pandas as pd

from app.business.ai.train import *


# for train & test data
def train(train_data_df):
    train_data_df = generate_filter_class(train_data_df)  # generate filter class
    x, y = generate_xy_class(train_data_df)  # generate data for train model

    from sklearn.model_selection import KFold
    kf = KFold(n_splits=10, random_state=RANDOM_STATE, shuffle=True)

    dfs = []
    for train_index, val_index in kf.split(x):  # split train test set

        x_train_val_ori, x_test_ori, y_train_val_ori, y_test_ori = split_data(x, y, train_index, val_index)
        x_test, y_test, x_train_val, y_train_val, x_test_ori = generate_train_data(x, x_train_val_ori, x_test_ori,
                                                                                   y_train_val_ori, y_test_ori)
        # fit model on train data and get accuracy of validation data
        model = LGBM_MODEL
        kf = KFold(n_splits=10, random_state=RANDOM_STATE, shuffle=True)
        accuracy_list = []
        for sub_train_index, sub_val_index in kf.split(x_train_val):
            x_train, x_val, y_train, y_val = split_data(x_train_val.values, y_train_val.values, sub_train_index,
                                                        sub_val_index)
            model.fit(x_train, y_train)
            predictions = model.predict(x_val)
            from sklearn.metrics import accuracy_score
            accuracy = accuracy_score(y_val, predictions)
            accuracy_list.append(accuracy)

        report_model(model, x_test, y_test, np.mean(accuracy_list))
        dfs.append(generate_df(model,x_test_ori,x_test,y_test))

    return pd.concat(dfs)

def generate_df(model,x_test_ori,x_test,y_test):
    df_new = x_test_ori.copy()
    df_new['실제클래스'] = y_test
    df_new['예측클래스'] = model.predict(x_test)
    df_new[['pred_proba=0', 'pred_proba=1', 'pred_proba=2']] = model.predict_proba(x_test).tolist()
    return df_new

def report_model(model, x_test, y_test, accuracy):
    from log import logger
    logger.info(f"[report] : %s" %accuracy)
    logger.info(f"accuracy : %s" %accuracy)
    from sklearn.metrics import classification_report
    logger.info(f"%s" %classification_report(y_test, model.predict(x_test)))
    from sklearn.metrics import roc_auc_score
    logger.info(f"roc_auc_score : %s" %roc_auc_score(y_test, model.predict_proba(x_test), multi_class='ovr'))


#TODO save model
def save_model(model, key_danger_index):
    import joblib
    joblib.dump(model, MODEL_PATH(key_danger_index))


def split_data(x, y, train_index, val_index):
    return x.values[train_index], x.values[val_index], y.values[train_index], y.values[val_index]


def generate_train_data(x, x_train_val_ori, x_test_ori, y_train_val_ori, y_test_ori):
    x_train_val_ori = pd.DataFrame(x_train_val_ori, columns=x.columns)
    y_train_val = pd.DataFrame(y_train_val_ori, columns=[KEY_FILTER_CLASS])
    x_test_ori = pd.DataFrame(x_test_ori, columns=x.columns)
    y_test = pd.DataFrame(y_test_ori, columns=[KEY_FILTER_CLASS])

    x_train_val = x_train_val_ori.iloc[:, 2:]
    x_test = x_test_ori.iloc[:, 2:]

    from sklearn.preprocessing import MinMaxScaler  # preprocessing
    scaler = MinMaxScaler()
    scaler.fit(x_train_val)
    x_train_val = pd.DataFrame(scaler.transform(x_train_val), columns=x_train_val.columns)
    x_test = pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)

    return x_test, y_test, x_train_val, y_train_val, x_test_ori


def generate_xy_class(df):
    return df.iloc[:, :-1], df[KEY_FILTER_CLASS]


def generate_filter_class(df):
    df.fillna(0, inplace=True)
    df['num'] = df['112신고데이터'] / df['생활인구']
    df.fillna(0, inplace=True)

    q1, q2, q3, q4 = np.percentile(df['num'], [25, 50, 75, 100])
    upper_fence = q3 + (1.5 * (q3 - q1))
    df[KEY_FILTER_CLASS] = np.digitize(x=df['num'], bins=[q2, upper_fence], right=True)  # generate filter class
    return df.drop(columns=['num'])

