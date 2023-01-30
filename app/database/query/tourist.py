from app.database.database import Database
from app.database.query.query import *


def select_all_tourist():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_TOURIST)
    database.close()
    return  result



def insert_tourist(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_TOURIST, data_record_list)
    database.commit()
    database.close()