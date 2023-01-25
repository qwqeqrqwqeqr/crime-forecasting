import psycopg2
import configparser



class Database:

    def __init__(self):
        config = configparser.ConfigParser()
        
        from app.database.config.constants import DB_CONFIG_PATH
        config.read(DB_CONFIG_PATH)
        self.db = psycopg2.connect("host = {host} dbname={name} user={user} password={password} port={port}".format(host=config['database']['DB_HOST'],name=config['database']['DB_NAME'],user=config['database']['DB_USER'],password=config['database']['DB_PASSWORD'],port=config['database']['DB_PORT']))
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

