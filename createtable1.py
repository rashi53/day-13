import sqlite3 as lite
cars=(
    (1,'Audi',52642),
    (2,'Mercedes',57127),
    (3,'skoda',9000),
    (4,'Volvo',29000),
    (5,'Bentley',350000),
    (6,'Hummer',41400),
    (7,'Volkswagen',21600)
     
)
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price Int)")
    cur.executemany("INSERT INTO Cars VALUES(?,?,?)",cars)
    
