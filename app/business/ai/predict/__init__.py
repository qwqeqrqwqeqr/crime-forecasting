from datetime import datetime

import numpy as np

from app.business.ai import KEY_FILTER_CLASS
from app.utils.constants import PATH_PREDICT_MODEL, PATH_PREDICT_SCALER

PREDICT_TRAIN_MODEL_PATH = PATH_PREDICT_MODEL+str(datetime.date.today())+".pkl"
PREDICT_TRAIN_SCALER_PATH = PATH_PREDICT_SCALER+str(datetime.date.today())+".pkl"



def generate_xy_class(df):
    return df.iloc[:, :-1], df[KEY_FILTER_CLASS]


def generate_filter_class(df):
    df.fillna(0, inplace=True)
    df['num'] = (df['112신고데이터'] + 0.0000000001) / df['생활인구']
    df.fillna(0, inplace=True)

    q1, q2, q3, q4 = np.percentile(df['num'], [25, 50, 75, 100])
    upper_fence = q3 + (1.5 * (q3 - q1))
    df[KEY_FILTER_CLASS] = np.digitize(x=df['num'], bins=[q2, upper_fence], right=True)  # generate filter class
    return df.drop(columns=['num'])