import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute('Use test;')
query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format('1214')
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
        
#help adhu        
        