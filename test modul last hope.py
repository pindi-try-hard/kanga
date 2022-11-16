from tkinter import*
import tkinter as tk
window=tk.Tk()
window.title("enter records")
import mysql.connector
mydb=mysql.connector.connect(host='localhost',passwd='kingfisher')
cursor = mydb.cursor()
while(1):
    try:
        cursor.execute("Create database test")
    except mysql.connector.errors.DatabaseError:
        
        break
while(1):
    try:
        cursor.execute("USE test")       
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
    except mysql.connector.errors.ProgrammingError :
        
        break
cursor.execute("use test")
lab1=Label(window,text='Admn number',font=("times new roman", 20)).grid(row=1,column=0)
lab2=Label(window,text='Name',font=("times new roman", 20)).grid(row=2,column=0)
lab3=Label(window,text='Age',font=("times new roman", 20)).grid(row=3,column=0)
lab4=Label(window,text='Gender(m/f)',font=("times new roman", 20)).grid(row=4,column=0)
lab5=Label(window,text='Height',font=("times new roman", 20)).grid(row=5,column=0)
lab6=Label(window,text='Weight',font=("times new roman", 20)).grid(row=6,column=0)
lab7=Label(window,text='Blood group',font=("times new roman", 20)).grid(row=7,column=0)
lab8=Label(window,text='If the patient had covid',font=("times new roman", 20)).grid(row=8,column=0)
lab9=Label(window,text='Did patient take vaccine(no of doses)',font=("times new roman", 20)).grid(row=9,column=0)
lab10=Label(window,text='Pre medical history',font=("times new roman", 20)).grid(row=10,column=0)
ent1=Entry(window)
ent1.grid(row=1,column=1)
ent2=Entry(window)
ent2.grid(row=2,column=1)
ent3=Entry(window)
ent3.grid(row=3,column=1)
ent4=Entry(window)
ent4.grid(row=4,column=1)
ent5=Entry(window)
ent5.grid(row=5,column=1)
ent6=Entry(window)
ent6.grid(row=6,column=1)
ent7=Entry(window)
ent7.grid(row=7,column=1)
ent8=Entry(window)
ent8.grid(row=8,column=1)
ent9=Entry(window)
ent9.grid(row=9,column=1)
#ent10=Entry(window)
#ent10.grid(row=10,column=1)
def display_input():
   a=var1.get()
   b=var2.get()
   c=var3.get()
   d=var4.get()
   e=var5.get()
   f=var6.get()
   g=var7.get()
   h=var8.get()
   
   print(a,b,c,d,e,f,g,h)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()

t1 = Checkbutton(window, text="cancer", variable=var1, onvalue='cancer', offvalue='')
t1.deselect()
t1.grid(row=10,column=1)
t2 = Checkbutton(window, text="high blood pressure", variable=var2, onvalue='high blood pressure', offvalue='')
t2.deselect()
t2.grid(row=11,column=1)
t3 = Checkbutton(window, text="diabetes", variable=var3, onvalue='diabetes', offvalue='')
t3.deselect()
t3.grid(row=12,column=1)
t4 = Checkbutton(window, text="high cholestrol", variable=var4, onvalue='high cholestrol', offvalue='')
t4.deselect()
t4.grid(row=13,column=1)
t5 = Checkbutton(window, text="Asthma or lung disease", variable=var5, onvalue='Asthma or lung disease', offvalue='')
t5.deselect()
t5.grid(row=14,column=1)
t6 = Checkbutton(window, text="Thyroid disease", variable=var6, onvalue='Thyroid disease', offvalue='')
t6.deselect()
t6.grid(row=15,column=1)
t7 = Checkbutton(window, text="Liver disease", variable=var7, onvalue='Liver disease', offvalue='')
t7.deselect()
t7.grid(row=16,column=1)
t8 = Checkbutton(window, text="Dementia", variable=var8, onvalue='Dementia', offvalue='')
t8.deselect()
t8.grid(row=17,column=1)
btn=Buttonbtn=Button(window,text="save data",command=display_input)
btn.grid(row=18,column=1)
def savedata():
    admn_number=ent1.get()
    name=ent2.get()
    age=ent3.get()
    sex=ent4.get()
    height=ent5.get()
    weight=ent6.get()
    blood_group=ent7.get()
    covid_vaccination=ent8.get()
    covid_vaccination_details=ent9.get()
    pre_medical_history=confirm
    cursor.execute('''insert into medical_records
     (admn_number,name,age,sex,height,weight,blood_group,covid_vaccination,
     covid_vaccination_details,pre_medical_history)'''
     "values('"+admn_number+"','"+name+"','"+age+"','"+sex+"','"+height+"','"+weight+"','"+blood_group+"','"+covid_vaccination+"','"+covid_vaccination_details+"','"+pre_medical_history+"')")
    mydb.commit()
    print("record inserted")
    myLabel=Label(window,text='record inserted')
    myLabel.grid(row=12,column=1)
btn=Button(window,text="save data",command=savedata)
btn.grid(row=11,column=2)

