from tkinter import *
from tkinter import messagebox
main_window=Tk()
main_window.geometry('300x300')
main_window.config(bg='light blue')
main_window.title('HOMEPAGE')

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
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
        NAME CHAR(200) NOT NULL,
        AGE INT,
        SEX CHAR(200),
        HEIGHT INT,
        WEIGHT INT,
        BLOOD_GROUP CHAR(200),
        COVID_VACCINATION CHAR(200),
        COVID_VACCINATION_DETAILS CHAR(200),
        PRE_MEDICAL_HISTORY CHAR(200))''')
        cursor.execute(sql)
    except mysql.connector.errors.ProgrammingError :
        
        break
cursor.execute("use test")
def INSERT():
    global new_window,ent1,ent2,ent3,ent5,ent6,clicked1,clicked
    new_window=Toplevel(main_window)
    new_window.title("enter records")
    new_window.config(background='light blue')
    lab1=Label(new_window,text='Admn number',font=("times new roman", 20)).grid(row=1,column=0)
    lab2=Label(new_window,text='Name',font=("times new roman", 20)).grid(row=2,column=0)
    lab3=Label(new_window,text='Age',font=("times new roman", 20)).grid(row=3,column=0)
    lab4=Label(new_window,text='Gender(m/f)',font=("times new roman", 20)).grid(row=4,column=0)
    lab5=Label(new_window,text='Height(in cms)',font=("times new roman", 20)).grid(row=5,column=0)
    lab6=Label(new_window,text='Weight(in kg)',font=("times new roman", 20)).grid(row=6,column=0)
    lab7=Label(new_window,text='Blood group',font=("times new roman", 20)).grid(row=7,column=0)
    lab8=Label(new_window,text='If the patient had covid',font=("times new roman", 20)).grid(row=8,column=0)
    lab9=Label(new_window,text='Did patient take vaccine(no of doses)',font=("times new roman", 20)).grid(row=9,column=0)
    lab10=Label(new_window,text='Pre medical history',font=("times new roman", 20)).grid(row=10,column=0)
    ent1=Entry(new_window)
    ent1.grid(row=1,column=1,)
    ent2=Entry(new_window)
    ent2.grid(row=2,column=1)
    ent3=Entry(new_window)
    ent3.grid(row=3,column=1)
    #ent4=Entry(new_window)
    #ent4.grid(row=4,column=1)
    ent5=Entry(new_window)
    ent5.grid(row=5,column=1)
    ent6=Entry(new_window)
    ent6.grid(row=6,column=1)
    #ent7=Entry(new_window)
    #ent7.grid(row=7,column=1)
    #ent8=Entry(new_window)
    #ent8.grid(row=8,column=1)
    #ent9=Entry(new_window)
    #ent9.grid(row=9,column=1)
    #ent10=Entry(new_window)
    #ent10.grid(row=10,column=1)
    t1 = Checkbutton(new_window, text="cancer", variable=var1, onvalue='cancer', offvalue='')
    #t1.deselect()
    t1.grid(sticky='W',row=10,column=1)
    t2 = Checkbutton(new_window, text="high-blood-pressure", variable=var2, onvalue='high-blood-pressure', offvalue='')
    #t2.deselect()
    t2.grid(sticky='W',row=10,column=2)
    t3 = Checkbutton(new_window, text="diabetes", variable=var3, onvalue='diabetes', offvalue='')
    #t3.deselect()
    t3.grid(sticky='W',row=12,column=1)
    t4 = Checkbutton(new_window, text="high-cholestrol", variable=var4, onvalue='high-cholestrol', offvalue='')
    #t4.deselect()
    t4.grid(row=12,column=2)
    t5 = Checkbutton(new_window, text="Asthma-or-lung disease", variable=var5, onvalue='Asthma-or-lung disease', offvalue='')
    #t5.deselect()
    t5.grid(sticky='W',row=14,column=1)
    t6 = Checkbutton(new_window, text="Thyroid-disease", variable=var6, onvalue='Thyroid-disease', offvalue='')
    #t6.deselect()
    t6.grid(sticky='W',row=14,column=2,)
    t7 = Checkbutton(new_window, text="Liver-disease", variable=var7, onvalue='Liver-disease', offvalue='')
    #t7.deselect()
    t7.grid(sticky='W',row=16,column=1)
    t8 = Checkbutton(new_window, text="Dementia", variable=var8, onvalue='Dementia', offvalue='')
    #t8.deselect()
    t8.grid(sticky='W',row=16,column=2)
    t9 = Checkbutton(new_window, text="NILL", variable=var9, onvalue='NILL', offvalue='')
    #t9.deselect()
    YES = Radiobutton(new_window,text="YES",variable=f,value='YES',command=vaccine())
    YES.grid(row=9,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=f,value='NO',command=vaccine())
    NO.grid(row=9,column=2,sticky="W")
    t9.grid(sticky='W',row=18,column=1)
    YES = Radiobutton(new_window,text="YES",variable=r,value='YES',command=COVID())
    YES.grid(row=8,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=r,value='NO',command=COVID())
    NO.grid(row=8,column=2,sticky="W")
    options = [
    "O -ve",
    "O +ve",
    "A -ve",
    "A +ve",
    "B -ve",
    "B +ve",
    "AB -ve",
    "AB +ve"
    ]
    clicked1 = StringVar()
    clicked1.set('choose your blood group')
    drop=OptionMenu(new_window,clicked1,*options )
    drop.grid(row=7,column=1,ipadx=85)
    options = [
    "MALE",
    "FEMALE",
    "RATHER NOT SAY"
    ]
    clicked = StringVar()
    clicked.set('M/F/O')
    drop=OptionMenu(new_window,clicked,*options )
    drop.grid(row=4,column=1,ipadx=85)
    btn=Button(new_window,text="save data",command=savedata)
    btn.grid(row=19,column=2)
    
    bmbtn=Button(new_window,text='FIND bmi',command=BMI)
    bmbtn.grid(row=19,column=1)
    btnquit=Button(new_window,text='quit',command=close)
    btnquit.grid(row=19,column=3)
    
def vaccine():
    return(f.get())
f=StringVar()

def COVID():
    return(r.get())
r=StringVar()


def blood_GROUP():
    return(clicked1.get())


def show():
    return(clicked.get())


def display_input():
   a=var1.get()
   b=var2.get()
   c=var3.get()
   d=var4.get()
   e=var5.get()
   f=var6.get()
   g=var7.get()
   h=var8.get()
   i=var9.get()
   values=a+' '+b+' '+c+' '+d+' '+e+' '+f+' '+g+' '+h+' '+i
   return values

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
def BMI():
    a=int(ent5.get())/100
    b=a*a
    BMI=int(ent6.get())/float(b)
    print('Your BMI is:',BMI)
    BMI=round(BMI,1)
    bmi_index(BMI)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-BMI_CALCULATOR',f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-BMI_CALCULATOR', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-BMI_CALCULATOR', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi-BMI_CALCULATOR', 'something went wrong!')   

def close():
    new_window.destroy()
    
def close1():
    main_window.destroy()

def savedata():
    admn_number=ent1.get()
    name=ent2.get()
    age=ent3.get()
    sex=show()
    height=ent5.get()
    weight=ent6.get()
    blood_group=blood_GROUP()
    covid_vaccination=COVID()
    covid_vaccination_details=vaccine()
    pre_medical_history=display_input()
    cursor.execute('''insert into medical_records
     (admn_number,name,age,sex,height,weight,blood_group,covid_vaccination,
     covid_vaccination_details,pre_medical_history)'''
     "values('"+admn_number+"','"+name+"','"+age+"','"+sex+"','"+height+"','"+weight+"','"+blood_group+"','"+covid_vaccination+"','"+covid_vaccination_details+"','"+pre_medical_history+"')")
    mydb.commit()
    myLabel=Label(new_window,text='record inserted')
    myLabel.grid(row=12,column=0)

btn6=Button(text='INSERT',command=INSERT).grid(row=1,column=0,padx=65,pady=100,ipadx=35,ipady=15)
btn7=Button(text='quit',command=close1).grid(row=2,column=0)



main_window.mainloop()
