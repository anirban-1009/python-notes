import sqlite3
con=sqlite3.connect("aiml.db")
cur=con.cursor()
cur.execute("create table cs(id INT, name VARCHAR(20))")
cur.execute("insert into cs values (45,'suk')")
con.commit()
cur.execute("select * from cs")
print(cur.fetchall())
con.close()