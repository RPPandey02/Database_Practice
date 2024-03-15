import mysql.connector as conn
import csv

mydb = conn.connect(host='localhost', user='root', passwd='mysql')

curr = mydb.cursor()

curr.execute("create table dbase1.tb1(ID INT(10), NAME VARCHAR(40), REGID INT(10), BRANCH VARCHAR(5), YEAR INT(4) )")

curr.execute('use dbase1')
curr.execute('show tables')
curr.execute("create database dbase1")
curr.execute("show databases")
print(curr.fetchall())

curr.execute('insert into dbase1.tb1 values(1,"rudra",1089,"cse",2021)')
curr.execute('select * from dbase1.tb1')
print(curr.fetchall())
curr = mydb.cursor()
curr.execute('create database glass_data_dbase2')
curr.execute('use glass_data_dbase2')
curr.execute('create table glass_data2(C1 INT(10),C2 float(10,5),C3 float(10,5),C4 float(10,5),C5 float(10,5),C6 float(10,5),C7 float(10,5),C8 float(10,5),C9 float(10,5),C10 float(10,5),C11 float(10,5),C12 INT(10))')


with open('glass (1).data','r') as f:
    a = csv.reader(f,delimiter='\n')
    for i in a:
        print(str(i[0]))
        curr.execute(f'insert into glass_data values ({str(i[0])})')


curr.execute('show tables')
curr.execute('select * from glass_data_dbase2.glass_data')
print(curr.fetchall())
