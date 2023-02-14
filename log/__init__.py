import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
from datetime import datetime
file_handler = logging.FileHandler("/log/log/{}.log".format(str(datetime.now())[:10]))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)