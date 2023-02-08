import pandas as pd

from app.business.ai.train import *


# for train & test data
def train(train_data_df):
    train_data_df = generate_filter_class(train_data_df)  # generate filter class
    x, y = generate_xy_class(train_data_df)  # generate data for train model
    x,scaler = generate_train_data(x)

    from lightgbm import LGBMClassifier
    model = LGBMClassifier(learning_rate=0.1, max_depth=6, n_estimators=400, num_leaves=15, random_state=42)
    model.fit(x, y)
    save_model(model)
    save_scaler(scaler)


def save_model(model):
    import joblib
    joblib.dump(model, PREDICT_TRAIN_MODEL_PATH)

def save_scaler(scaler):
    from pickle import dump
    dump(scaler, open(PREDICT_TRAIN_SCALER_PATH, 'wb'))

def generate_train_data(x):
    x_train = x.iloc[:, 2:]
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    return  pd.DataFrame(scaler.transform(x_train), columns=x_train.columns),scaler






