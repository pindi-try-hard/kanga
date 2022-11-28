#from tkinter import *

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger')
cursor=mydb.cursor()
a=int(input('Enter admn no:'))
cursor.execute('USE TEST;')
cursor.execute(' Select * from medical_records;')
k=cursor.fetchall()
mydb.commit()

flag=0
for i in range(len(k)):
    m=list(k[i])
    if m[0]==a:
        flag=True
        

if flag==0:
    print('NO RECORD')
else:
    print(a)
    print(m)
    


    

