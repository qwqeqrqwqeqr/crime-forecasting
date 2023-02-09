from datetime import datetime
from app.utils.constants import PATH_PREDICT_TRAIN_DATA
PREDICT_TRAIN_DATA_PATH = PATH_PREDICT_TRAIN_DATA + str(datetime.date.today()) + ".csv"



from app.utils.constants import PATH_PREDICT_TEST_DATA
PREDICT_TEST_DATA_PATH = PATH_PREDICT_TEST_DATA + str(datetime.date.today()) + ".csv"


from app.utils.constants import PATH_PREDICT_RESULT_DATA
PREDICT_RESULT_DATA_PATH = PATH_PREDICT_RESULT_DATA + str(datetime.date.today()) + ".csv"