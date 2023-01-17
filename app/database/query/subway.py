from app.database.database import Database
from app.database.query.constants import *


def select_all_subway():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_SUBWAY)
    database.close()
    return  result



def insert_subway(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_SUBWAY, data_record_list)
    database.commit()
    database.close()