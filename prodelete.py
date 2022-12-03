'''import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
mycursor = mydb.cursor()
mycursor.execute("USE TEST")
mycursor = mydb.cursor()
sql = ("DELETE FROM EMPLOYEE WHERE INCOME = '50000'")
mycursor.execute(sql)
mydb.commit()'''

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
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
        
while flag==0:
    if flag==0:
        print('NO RECORD')
        break
else:
    print(a)
    print(m)
    ADMN_NUMBER=int(input("Enter the patients admn number:"))
    sql_update="delete from medical_records where admn_number=%s"
    val=(ADMN_NUMBER,)
    cursor.execute(sql_update,val)
    print("RECORDS HAS BEEN DELETED")
    mydb.commit()