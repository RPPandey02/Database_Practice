import sqlite3
db = sqlite3.connect("test.db")
curr = db.cursor()
# # curr.execute('create table tb1(name text , roll int , marks real)')
# curr.execute("insert into tb1 values('aas' , 24 , 563.45)")
# curr.execute("insert into tb1 values('akagtss' , 29 , 563.45)")
# curr.execute("insert into tb1 values('akrwteas' , 28 , 56.45)")
# curr.execute("insert into tb1 values('akfas' , 45 , 563.5)")
# curr.execute("insert into tb1 values('atgfr' , 55 , 63.45)")

check1 = curr.execute("select * from tb1")
for i in check1:
    print(i)
print("------------------------------------")
for r in (curr.execute("select * from tb1 where marks > 400")):
    print(r)



# commit all work in whole database
db.commit()
# # to close the connection
# db.close()


