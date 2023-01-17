from app.database.database import Database
from app.database.query.constants import QUERY_GET_ALL_IN_CONGESTION


def get_all_congestion():
    database= Database()
    result =database.execute(QUERY_GET_ALL_IN_CONGESTION)
    database.close()
    return  result









