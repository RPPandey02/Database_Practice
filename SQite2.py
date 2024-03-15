# creating 2 table
import sqlite3

db = sqlite3.Connection('db1')
curr = db.cursor()

# # table1
# # curr.execute("create table class1(name text , roll int , marks real)")
# curr.execute("insert into class1 values('rudra' , 24 , 75)")
# curr.execute("insert into class1 values('alok' , 23 , 84)")
# curr.execute("insert into class1 values('ankit' , 22 , 85)")
# curr.execute("insert into class1 values('shawat' , 21 , 89)")

db.commit()

# #table2
# # curr.execute("create table class2(name text , roll int , marks real)")
# curr.execute("insert into class2 values('akshat' , 14 , 73)")
# curr.execute("insert into class2 values('ayushaman' , 13 , 75)")
# curr.execute("insert into class2 values('abhnav' , 12 , 77)")
# curr.execute("insert into class2 values('akram' , 11 , 99)")



db.commit()

# cl1 = curr.execute("select * from class1")
# for i in cl1:
#     print(i)
# print("-----------------------------------------------------------------------------------")
# cl2 = curr.execute("select * from class2")
# for r in cl2:
#     print(r)


