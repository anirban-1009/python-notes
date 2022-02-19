import sqlite3
con=sqlite3.connect("aiml.db")
cur=con.cursor()
cur.execute("create table cs(id INT, name VARCHAR(20)),")
cur.execute("insert inro cs values (45, 'suk')")
con.commit()
cur.execute("select * from cs")
print(cur.fetchall())
con.close()
"""
create table midmarks(hno INT, name VARCHAR(20),python INT,ds INT,coa INT)
insert into midmarks values(6601, 'anirudh', 20,21,22)"""