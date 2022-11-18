import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute("USE TEST")
sql =('''CREATE TABLE MEDICAL_RECORDS(
   ADMN_NUMBER INT PRIMARY KEY,
   NAME CHAR(20) NOT NULL,
   AGE INT,
   SEX CHAR(1),
   HEIGHT INT,
   WEIGHT INT,
   BLOOD_GROUP CHAR(20),
   COVID_VACCINATION CHAR(100),
   COVID_VACCINATION_DETAILS CHAR(100),
   PRE_MEDICAL_HISTORY CHAR(100))''')
cursor.execute(sql)
mydb.close()
print("TABLE HAS BEEN CREATED")
