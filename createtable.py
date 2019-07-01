import sqlite3 as lite
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute('''CREATE TABLE Cars(
     Id INT,Name TEXT,Price Int)''')
    print("table cars created")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',52127)")
    print("values in table car inserted")
    
