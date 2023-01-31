# Model Parameter
KEY_FILTER_CLASS = 'filter_class'
RANDOM_STATE = 42
C=100.0
PENALTY='l2'
SOLVER ='lbfgs'



import datetime
from app.utils.constants import PATH_TRAIN_MODEL

def MODEL_PATH(key_danger_index) :
    return PATH_TRAIN_MODEL+str(datetime.date.today())+key_danger_index+".pkl"