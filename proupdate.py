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
    var1=input("enter patients name:")
    var2=int(input("enter patients age:"))
    var3=input("enter patients gender:")
    var4=int(input("height:"))
    var5=int(input("weight:"))
    var6=input("blood_group:")
    var7=input("covid_vaccination:")
    var8=input("covid_vaccination details:")
    var9=input("premedical_history:")

    sql_update = '''UPDATE MEDICAL_RECORDS SET NAME=%s, AGE=%s, SEX=%s, HEIGHT=%s, WEIGHT=%s, 
                BLOOD_GROUP=%s, COVID_VACCINATION=%s, COVID_VACCINATION_DETAILS=%s, PRE_MEDICAL_HISTORY=%s 
                WHERE ADMN_NUMBER=%s'''
    val =  (var1, var2, var3, var4, var5, var6, var7, var8, var9, ADMN_NUMBER)
    cursor.execute(sql_update, val)
    print("RECORD HAS BEEN UPDATED")
    mydb.commit()
'''import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute("USE TEST")
sql =("UPDATE MEDICAL_RECORDS WHERE ADMN_NUMBER='69420'")
cursor.execute(sql)'''

'''ADMN_NUMBER=int(input("Enter the patients admn number"))
var1=input("enter patients name")
var2=int(input("enter patients age"))
var3=input("enter patients gender")
var4=int(input("height"))
var5=int(input("weight"))
var6=input("blood_group")
var7=input("covid_vaccination")
var8=input("covid_vaccination details")
var9=input("premedical_histor")

sql_update = "UPDATE MEDICAL_RECORDS SET NAME=%s, AGE=%s, SEX=%s, HEIGHT=%s, WEIGHT=%s, BLOOD_GROUP=%s, COVID_VACCINATION=%s, COVID_VACCINATION_DETAILS=%s, PRE_MEDICAL_HISTORY=%s WHERE ADMN_NUMBER=%s"
val =  (var1, var2, var3, var4, var5, var6, var7, var8, var9, ADMN_NUMBER)
cursor.execute(sql_update, val)
mydb.commit()'''