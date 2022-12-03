import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE HELP_ADHU")
mydb.commit()
cursor.execute("CREATE DATABASE HELP_GURU")
