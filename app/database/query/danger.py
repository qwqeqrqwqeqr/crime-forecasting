from app.database.database import Database
from app.database.query.constants import *


def select_all_danger():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_DANGER)
    database.close()
    return  result


def insert_danger(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_DANGER, data_record_list)
    database.commit()
    database.close()

