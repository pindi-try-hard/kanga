import mysql.connector
y=int(input("Enter the patients admn number:"))
n=input("Enter the patients name:")
a=int(input("ENter the patients age:"))
s=input("enter m or f:")
h=int(input("height in cms"))
w=int(input("weight in kgs"))
b=input("enter persons blood group")
c=input("enetr covid:")
cd=input("enter covid details:")
p=input("if pre medical histor ne:")
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute("USE TEST")
sql='''INSERT INTO MEDICAL_RECORDS(
    ADMN_NUMBER,NAME,AGE,SEX,HEIGHT,WEIGHT,BLOOD_GROUP,
    COVID_VACCINATION,COVID_VACCINATION_DETAILS,PRE_MEDICAL_HISTORY)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
data=(y,n,a,s,h,w,b,c,cd,p)
cursor.execute(sql,data)
mydb.commit()
print("data inserted")
n=input("Do you want to see all records entered so far(y/n)")
if n=='y':
    print("here are the current entries")
    cursor.execute("SELECT*FROM MEDICAL_RECORDS")
    for MEDICAL_RECORDS in cursor:
        print(MEDICAL_RECORDS)
