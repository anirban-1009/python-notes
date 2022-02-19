#new14.py

import sqlite3
con=sqlite3.connect("aiml.db")
cur=con.cursor()
cur.execute("create table midmarks(hno INT,name VARCHAR(20),python INT,ds INT,coa INT)")
cur.execute("insert into midmarks values(6601,'anirudh',20,21,22)")
cur.execute("insert into midmarks values(6602,'nithin',21,23,18)")
con.commit()
cur.execute("select * from midmarks ")
print(cur.fetchall())
con.close()