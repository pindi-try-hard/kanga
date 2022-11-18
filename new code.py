'''from tkinter import *
master=Tk()
Label(master,text="Enter the patient's admn number:").grid(row=0)
Label(master,text="Enter the patient's name:").grid(row=1)
Label(master,text="Enter the patient's age:").grid(row=2)
Label(master,text="Enter the patient's gender(m/f):").grid(row=3)
Label(master,text="Enter the patient's height(in cms):").grid(row=4)
Label(master,text="Enter the patient's weight(in kg):").grid(row=5)
Label(master,text="Enter the patient's blood group:").grid(row=6)
Label(master,text="Enter if patient's had covid:").grid(row=7)
Label(master,text="Enter if patient's has taken vaccine(and no.of doses):").grid(row=8)
Label(master,text="Enter the patient's pre medical history:").grid(row=9)
Label()
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e5=Entry(master)
e6=Entry(master)
e7=Entry(master)
e8=Entry(master)
e9=Entry(master)
e10=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
e8.grid(row=7,column=1)
e9.grid(row=8,column=1)
e10.grid(row=9,column=1)'''

from tkinter import*
master=Tk()
Label(master,text="Enter the patient's admn number:")
e1=Entry(master,width=50)
e1.pack()
def myclick():
    myLabel=Label(master,text='record inserted')
    myLabel.pack()
myButton=Button(master,text='SUBMIT',command=myclick)
myButton.pack()
master.mainloop()

import mysql.connector

mydb=mysql.connector.connect(host='localhost',passwd='kingfisher')
cursor = mydb.cursor()
cursor.execute("USE TEST")
x='y'
while x == "y":
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
    sql='''INSERT INTO MEDICAL_RECORDS(
        ADMN_NUMBER,NAME,AGE,SEX,HEIGHT,WEIGHT,BLOOD_GROUP,
        COVID_VACCINATION,COVID_VACCINATION_DETAILS,PRE_MEDICAL_HISTORY)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    data=(e1,e2,e4,e5,e6,e7,e8,e9)
    cursor.execute(sql,data)
    mydb.commit()
    print("data inserted")
    n=input("Enter another data(y/n):")
    x=n
    
