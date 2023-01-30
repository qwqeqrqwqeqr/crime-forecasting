from app.database.database import *
from app.database.query.query import *


def get_all_congestion():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_CONGESTION)
    database.close()
    return  result

def insert_congestion(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_CONGESTION, data_record_list)
    database.commit()
    database.close()








