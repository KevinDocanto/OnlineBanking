import sqlite3
import os.path


class DB:
    def __init__(self):  
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "db/client.db")
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()


    def execute1(self, data):
        self.c.execute(data)
        self.conn.commit()

    def execute2(self, data, detail):
        self.c.execute(data, detail)
        self.conn.commit()
    
    def close(self):
        return self.conn.close()