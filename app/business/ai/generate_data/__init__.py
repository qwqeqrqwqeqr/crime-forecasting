
import datetime

from app.utils.constants import PATH_TRAIN_DATA


def TRAIN_DATA_PATH(key_danger_index) :
    return PATH_TRAIN_DATA+str(datetime.date.today())+"_"+key_danger_index.replace('_','-')+".csv"

