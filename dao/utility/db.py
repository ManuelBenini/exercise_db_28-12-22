import mysql.connector as mysql
import json

from pathlib import Path

class MySql:

    @classmethod
    def openConnection(cls):
        config = json.loads(Path(r"dao\utility\c.json").read_text())
        cls.conn = mysql.connect(**config)
        cls.cursor = cls.conn.cursor()
        return cls.cursor
  
    @classmethod
    def query(cls, query):
        cls.cursor.execute(query)
        
    @classmethod
    def getResults(cls):
        return cls.cursor.fetchall()
    
    @classmethod
    def closeConnection(cls):
        cls.cursor.close()
        cls.conn.close()
        
    @classmethod
    def commit(cls):
        cls.conn.commit()
    
      
    



