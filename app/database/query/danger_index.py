from app.database.database import Database
from app.database.query.query import *


def select_all_danger_index():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_DANGER_INDEX)
    database.close()
    return  result


def insert_danger_index(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_DANGER_INDEX, data_record_list)
    database.commit()
    database.close()

