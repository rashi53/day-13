import sqlite3 as lite
import sys
try:
    con=lite.connect('test.db')
    cur=con.cursor()
    cur.executescript("""
     DROP TABLE IF EXISTS Cars;
     CREATE TABLE Cars(Id INT,Name TEXT,Price Int);
     INSERT INTO Cars VALUES(6,'Citroen',21000);
     INSERT INTO Cars VALUES(7,'Hummer',41400);
     INSERT INTO Cars VALUES(8,'Volkswagen',21600);
     """)
    con.commit()
except lite.Error as e:
    if e:
        con.rollback()
    print("Error %s:"%e.args[0])
    sys.exit(1)
finally:
          if con:
           con.close()
