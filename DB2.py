import mysql.connector as conn
import csv

mydb = conn.connect(host='localhost', user='root', passwd='mysql')

curr = mydb.cursor()
curr.execute('use dbase1')

# show data with filter
curr.execute("select * from tb1 from db1 WHERE col1 = 1 ")

curr.execute("select * from tb1.db1 WHERE col2 LIKE '1.51%")

# show data from a instance of another table with filter
curr.execute("select * from (select * from tb1.db1) WHERE col1>4")

# sort the data
curr.execute("select * from tb1.db1 group by col1 having count (col1)>2")

# UPDATE in a table
curr.execute("UPDATE tb1.db1 SET col1=6 , col2 = 8 WHERE col1= 1")

# DROP
curr.execute("table tb1.db1")