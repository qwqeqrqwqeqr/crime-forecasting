from app.database.database import Database
from app.database.query.constants import *


def select_all_report():
    database= Database()
    result =database.execute(QUERY_SELECT_ALL_REPORT)
    database.close()
    return  result



def insert_report(data_record_list):
    database = Database()
    database.executeMany(QUERY_INSERT_REPORT, data_record_list)
    database.commit()
    database.close()