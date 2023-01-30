from app.database.database import Database
from app.database.query.query import *


def select_all_hangang():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_HANGANG)
    database.close()
    return  result


def insert_hangang(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_HANGANG, data_record_list)
    database.commit()
    database.close()