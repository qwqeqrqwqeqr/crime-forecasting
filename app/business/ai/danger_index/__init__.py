# Model Parameter

RANDOM_STATE = 42





import datetime

from app.utils.constants import PATH_DANGER_INDEX_MODEL
DANGER_INDEX_MODEL_PATH = lambda key_danger_index : PATH_DANGER_INDEX_MODEL+str(datetime.date.today())+"_"+key_danger_index.replace('_','-')+".pkl"


from app.utils.constants import PATH_SR_DANGER_INDEX_MODEL
SR_DANGER_INDEX_MODEL_PATH = PATH_SR_DANGER_INDEX_MODEL+str(datetime.date.today())+".pkl"