import evadb
import pandas as pd


class DbEntity:
    def __init__(self):
        self.cursor = evadb.connect().cursor()

    def initalize_db(self):
        self.cursor.query("""
        DROP TABLE IF EXISTS Temporary;
        """).df()

        self.cursor.query("""
            CREATE TABLE IF NOT EXISTS Temporary (
                Date TEXT(5000),
                Symbol TEXT(5000),
                Series TEXT(5000),
                Open FLOAT,
                High FLOAT,
                Low FLOAT,
                Last FLOAT,
                Close FLOAT,
                VWAP FLOAT
            );
        """).df()

        print("Table is created!!!")

        print(self.cursor.query("SHOW FUNCTIONS;").df())
        print(self.cursor.show("tables").df())


        self.cursor.query("LOAD CSV 'result.csv' INTO Temporary").df()
        self.cursor.query("SELECT * FROM Temporary").df()
        print(self.cursor.show("tables").df())

dbEntity = DbEntity()
dbEntity.initalize_db()
