import pandas as pd
import psycopg2


if __name__ == '__main__':
    host = '121.131.185.164'
    port = '5435'
    dbname = 'postgres'
    username = 'ncyc'
    pwd = 'ncyc0078@@'

    conn = psycopg2.connect(
        "host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))

    sql = "select * from public.congestion;"
    df = pd.read_sql_query(sql, conn)
    df.to_csv("./congestion202201.csv")