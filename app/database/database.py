import psycopg2
from app.config.production import *
class Database:

    def __init__(self):
        self.db = psycopg2.connect("host = {host} dbname={name} user={user} password={password} port={port}".format(host=DB_HOST,name=DB_NAME,user=DB_USER,password=DB_PASSWORD,port=DB_PORT))
        self.cursor = self.db.cursor()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row


    def executeMany(self,query,args={}):
        self.cursor.executemany(query,args)

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()
        self.cursor.close()

