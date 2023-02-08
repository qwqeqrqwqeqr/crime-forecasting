# Model Parameter
KEY_FILTER_CLASS = 'filter_class'
RANDOM_STATE = 42



from sklearn.linear_model import LogisticRegression
LR_MODEL = LogisticRegression(random_state=RANDOM_STATE, C=100.0, penalty='l2', solver='lbfgs')


import datetime
from app.utils.constants import PATH_TRAIN_MODEL

def MODEL_PATH(key_danger_index) :
    return PATH_TRAIN_MODEL+str(datetime.date.today())+"_"+key_danger_index.replace('_','-')+".pkl"