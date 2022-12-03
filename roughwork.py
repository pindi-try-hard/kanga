import tkinter as tk
import mysql.connector
from tkinter import *
def submitact():
    user = Username.get()
    passw = password.get()
    print(f"The name entered by you is {user} {passw}")
    logintodb(user, passw)
def logintodb(user, passw):
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="test")
        cursor = db.cursor()
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="test")
        cursor = db.cursor()
    savequery = "select * from medical_records"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query Executed successfully")
         
    except:
        db.rollback()
        print("Error occurred")
  
 
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
submitbtn = tk.Button(root, text ="Login",
bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
root.mainloop()
