import sqlite3

class Conn:
    def __init__(self, db_name="test.db"):
        self._db_name = db_name
        
    def __enter__(self):
        try:
            self._conn = sqlite3.connect(self._db_name)
            print(f"Open database {self._db_name} successfully")
        except:
            print(f"Failed to open database {self._db_name}")

        return self._conn

    def __exit__(self, type, value, traceback):
        self._conn.close()
        
with Conn() as conn:
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
    conn.commit()
    print ("数据表创建成功")