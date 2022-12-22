
from tkinter import *
from tkinter import messagebox
import tkinter as tk
main_window=tk.Tk()
main_window.geometry('240x200')
main_window.title('Medical Records Maintenance')

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher')
cursor=mydb.cursor()
while(1):
    try:
        cursor.execute('CREATE DATABASE TEST;')
    except mysql.connector.errors.DatabaseError:
        break

while(1):
    try:
        cursor.execute('USE TEST')
        sql=('''CREATE TABLE MEDICAL_RECORDS(
        ADMN_NUMBER INT(200) PRIMARY KEY,
        NAME CHAR(130) NOT NULL,
        AGE INT(3),
        GENDER CHAR(50),
        DATE_OF_BIRTH VARCHAR(200),
        HEIGHT INT(10),
        WEIGHT INT(10),
        BLOOD_GROUP CHAR(10),
        COVID_STATUS CHAR(5),
        COVID_VACCINATION_STATUS CHAR(15),
        PAST_HISTORY CHAR(150))''')
        cursor.execute(sql)
    except mysql.connector.errors.ProgrammingError:
        break

cursor.execute('USE TEST;')
def INSERT():
    global new_window,ent1,ent2,ent3,ent6,ent7,ent12,ent14,c1,c2,c3,c4,c5,f,r
    new_window=Toplevel(main_window)
    new_window.title('ENTER RECORD')
    l=['ADMN NUMBER','NAME','AGE','GENDER','DOB','HEIGHT(cm)','WEIGHT(kg)','BLOOD GROUP',
       'COVID STATUS','COVID VACCINATION STATUS','Past History','Any major illness/operations in past',
       'Using any implant/accessories']
    f='times new roman'
    
    lab1=Label(new_window,text=l[0],font=(f,13)).grid(row=0,column=0)
    lab2=Label(new_window,text=l[1],font=(f,13)).grid(row=1,column=0)
    lab3=Label(new_window,text=l[2],font=(f,13)).grid(row=2,column=0)
    lab4=Label(new_window,text=l[3],font=(f,13)).grid(row=3,column=0)
    lab5=Label(new_window,text=l[4],font=(f,13)).grid(row=4,column=0)
    lab6=Label(new_window,text=l[5],font=(f,13)).grid(row=5,column=0)
    lab7=Label(new_window,text=l[6],font=(f,13)).grid(row=6,column=0)
    lab8=Label(new_window,text=l[7],font=(f,13)).grid(row=7,column=0)
    lab9=Label(new_window,text=l[8],font=(f,13)).grid(row=8,column=0)
    lab10=Label(new_window,text=l[9],font=(f,13)).grid(row=9,column=0)
    lab11=Label(new_window,text=l[10],font=(f,13)).grid(row=10,column=0)
    lab12=Label(new_window,text='').grid(row=11,column=0)
    lab13=Label(new_window,text=l[11],font=(f,13)).grid(row=12,column=0)
    lab14=Label(new_window,text=l[12],font=(f,13)).grid(row=13,column=0)

    ent1=Entry(new_window)
    ent1.grid(row=0,column=1)
    ent2=Entry(new_window)
    ent2.grid(row=1,column=1)
    ent3=Entry(new_window)
    ent3.grid(row=2,column=1)
    ent6=Entry(new_window)
    ent6.grid(row=5,column=1)
    ent7=Entry(new_window)
    ent7.grid(row=6,column=1)
    ent12=Entry(new_window)
    ent12.grid(row=12,column=1)
    ent14=Entry(new_window)
    ent14.grid(row=16,column=1)

    t1 = Checkbutton(new_window, text="Jaundice", variable=var1, onvalue='Jaundice', offvalue='')
    t1.grid(sticky='W',row=10,column=1)
    t2 = Checkbutton(new_window, text="Allergies", variable=var2, onvalue='Allergies', offvalue='')
    t2.grid(sticky='W',row=10,column=2)
    t3 = Checkbutton(new_window, text="Blood Transfusion", variable=var3, onvalue='Blood Transfusion', offvalue='')
    t3.grid(sticky='W',row=11,column=1)
    t4 = Checkbutton(new_window, text="NIL", variable=var7, onvalue='NIL', offvalue='')
    t4.grid(sticky='W',row=11,column=2)
    t5 = Checkbutton(new_window, text="Dental implant", variable=var4, onvalue='Dental implant', offvalue='')
    t5.grid(sticky='W',row=13,column=1)
    t6 = Checkbutton(new_window, text='Braces', variable=var5, onvalue='Braces', offvalue='')
    t6.grid(sticky='W',row=13,column=2)
    t7 = Checkbutton(new_window, text="Spectacles", variable=var6, onvalue='Spectacles', offvalue='')
    t7.grid(sticky='W',row=14,column=1)
    t8 = Checkbutton(new_window, text="NIL", variable=var6, onvalue='NIL', offvalue='')
    t8.grid(sticky='W',row=14,column=2)

    blood=['O -ve','O +ve','A -ve','A +ve','B -ve','B +ve','AB -ve','AB +ve']
    gender=['Male','Female','Other']
    date=[]
    for i in range(1,32):
        date.append(i)
    months=['January','February','March','April','May','June','July','August','September','October',
    'Novermber','December']
    year=[]
    for i in range(1940,2050):
        year.append(i)

    c1=StringVar()
    c1.set('BLOOD GROUP')
    c2=StringVar()
    c2.set('M/F/O')
    c3=StringVar()
    c3.set('Date')
    c4=StringVar()
    c4.set('Month')
    c5=StringVar()
    c5.set('Year')
    d1=OptionMenu(new_window,c1,*blood)
    d2=OptionMenu(new_window,c2,*gender)
    d3=OptionMenu(new_window,c3,*date)
    d4=OptionMenu(new_window,c4,*months)
    d5=OptionMenu(new_window,c5,*year)
    d1.grid(row=7,column=1)
    d2.grid(row=3,column=1)
    d3.grid(sticky='W',row=4,column=1)
    d4.grid(sticky='E',row=4,column=1)
    d5.grid(sticky='W',row=4,column=2)

    def dell():
        msg_box=tk.messagebox.askquestion('Enter Record','Click yes to save')
        if msg_box=='yes':
            savedata()

    b1=Button(new_window,text="Enter",command=dell,bg='light grey')
    b2=Button(new_window,text='Find BMI',command=BMI,bg='light grey')
    b3=Button(new_window,text='Exit',command=close,bg='light grey')
    b1.grid(sticky='E',row=20,column=2)
    b2.grid(row=6,column=2)
    b3.grid(sticky='W',row=20,column=3)

    f=StringVar()
    YES = Radiobutton(new_window,text="YES",variable=f,value='Yes',command=vaccine())
    YES.grid(row=8,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=f,value='No',command=vaccine())
    NO.grid(row=8,column=2,sticky="N")

    r=StringVar()
    YES = Radiobutton(new_window,text="YES",variable=r,value='Yes',command=vaccine())
    YES.grid(row=9,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=r,value='No',command=vaccine())
    NO.grid(row=9,column=2,sticky="N")

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()

def view():
    admn=IntVar()
    import tkinter as tk
    cursor = mydb.cursor()
    view=tk.Tk()
    view.title('Details')
    view.geometry('500x300')
    lab1=Label(view,text='ADMN NUMBER :',font=("times new roman", 13)).grid(row=1,column=0)
    e1=Entry(view,textvariable=admn)
    e1.grid(row=1,column=1)
    btn9=Button(view,text='VIEW',command=lambda:[disp(),bt0()],bg='light grey')
    btn9.grid(row=1,column=2)
    

    def disp():
        nonlocal admn
        a=e1.get()
        cursor.execute('Use test;')
        query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
        cursor.execute(query)
        data=cursor.fetchall()
        mydb.commit()

        if data!=[]:
            lab2=Label(view,text='NAME :',font=("times new roman", 13)).grid(row=2,column=0)
            lab3=Label(view,text='AGE :',font=("times new roman", 13)).grid(row=3,column=0)
            lab4=Label(view,text='GENDER :',font=("times new roman", 13)).grid(row=4,column=0)
            lab4=Label(view,text='DATE OF BIRTH :',font=("times new roman", 13)).grid(row=5,column=0)
            lab5=Label(view,text='HEIGHT(cm) :',font=("times new roman", 13)).grid(row=6,column=0)
            lab6=Label(view,text='WEIGHT(kg) :',font=("times new roman", 13)).grid(row=7,column=0)
            lab7=Label(view,text='BLOOD GROUP :',font=("times new roman", 13)).grid(row=8,column=0)
            lab8=Label(view,text='COVID STATUS :',font=("times new roman", 13)).grid(row=9,column=0)
            lab9=Label(view,text='COVID VACCINATION STATUS :',font=("times new roman", 13)).grid(row=10,column=0)
            lab10=Label(view,text='PAST HISTORY :',font=("times new roman", 13)).grid(row=11,column=0)
            for i in range(1):
                p=list(data[i])
                name=(p[1])
                age=(p[2])
                gender=(p[3])
                date_of_birth=(p[4])
                height=(p[5])
                weight=(p[6])
                blood_group=(p[7])
                covid_status=(p[8])
                covid_vaccination_status=(p[9])
                past_history=(p[10])

            t='times new roman'
            e2=Label(view,text=name,font=(t,13)).grid(row=2,column=1)
            e3=Label(view,text=age,font=(t,13)).grid(row=3,column=1)
            e4=Label(view,text=gender,font=(t,13)).grid(row=4,column=1)
            e5=Label(view,text=date_of_birth,font=(t,13)).grid(row=5,column=1)
            e6=Label(view,text=height,font=(t,13)).grid(row=6,column=1)
            e7=Label(view,text=weight,font=(t,13)).grid(row=7,column=1)
            e8=Label(view,text=blood_group,font=(t,13)).grid(row=8,column=1)
            e9=Label(view,text=covid_status,font=(t,13)).grid(row=9,column=1)
            e10=Label(view,text=covid_vaccination_status,font=(t,13)).grid(row=10,column=1)
            e11=Label(view,text=past_history,font=(t,13)).grid(row=11,column=1)
        else:
            view.destroy()
            messagebox.showerror('OOPS','NO RECORD')
            
    def close2():
            view.destroy()
    def bt0():
        try:
            btn9.destroy()
        except:
            pass
    btn1=Button(view,text='QUIT',command=close2,bg='light grey').grid(row=11,column=2)

def vaccine():
    return f.get()

def COVID():
    return r.get()

def blood_GROUP():
    return c1.get()

def gender():
    return c2.get()

def dob():
    a=c3.get()
    b=c4.get()
    c=c5.get()
    val=a+'  '+b+' '+c
    return val

def viewlay_input():
   a=var1.get()
   b=var2.get()
   c=var3.get()
   d=var4.get()
   e=var5.get()
   f=var6.get()
   g=var7.get()
   values=a+' '+b+' '+c+' '+d+' '+e+' '+f+' '+g
   return values

def BMI():
    a=int(ent6.get())/100
    b=a*a
    BMI=int(ent7.get())/float(b)
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
    Name=name.title()
    age=ent3.get()
    Gender=gender()
    Dob=dob()
    height=ent6.get()
    weight=ent7.get()
    blood_group=blood_GROUP()
    covid_status=COVID()
    covid_vaccination_status=vaccine()
    past_history=viewlay_input()
    try:
        cursor.execute('USE TEST')
        cursor.execute('''insert into medical_records
         (admn_number,name,age,gender,date_of_birth,height,weight,blood_group,covid_status,
         covid_vaccination_status,past_history)'''
         "values('"+admn_number+"','"+Name+"','"+age+"','"+Gender+"','"+Dob+"','"+height+"','"+weight+"','"+blood_group+"','"+covid_status+"','"+covid_vaccination_status+"','"+past_history+"')")
        mydb.commit()
        messagebox.showinfo('Success','Record inserted')
    except:
        messagebox.showerror('duplicate error','Record already exists')


def dlt():
    admn=IntVar()
    import tkinter as tk
    cursor=mydb.cursor()
    dlte=tk.Tk()
    dlte.title('Delete')
    dlte.geometry('500x300')
    f='times new roman'
    lab1=Label(dlte,text='ADMN NUMBER:',font=(f,13))
    lab1.grid(row=1,column=0)
    e1=Entry(dlte,textvariable=admn)
    e1.grid(row=1,column=1)
    btnn=Button(dlte,text='FIND',command=lambda:[disp(),butnboom()],bg='light grey')
    btnn.grid(row=1,column=2)
    
    def butnboom():
        try:
            btnn.destroy()
        except:
            pass
    def disp():
        nonlocal admn
        a=e1.get()
        cursor.execute('Use test;')
        query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
        cursor.execute(query)
        data=cursor.fetchall()
        mydb.commit()
        
        if data!=[]:
            lab2=Label(dlte,text='NAME :',font=("times new roman", 13)).grid(row=2,column=0)
            lab3=Label(dlte,text='AGE :',font=("times new roman", 13)).grid(row=3,column=0)
            lab4=Label(dlte,text='GENDER :',font=("times new roman", 13)).grid(row=4,column=0)
            lab4=Label(dlte,text='DATE OF BIRTH :',font=("times new roman", 13)).grid(row=5,column=0)
            lab5=Label(dlte,text='HEIGHT(cm) :',font=("times new roman", 13)).grid(row=6,column=0)
            lab6=Label(dlte,text='WEIGHT(kg) :',font=("times new roman", 13)).grid(row=7,column=0)
            lab7=Label(dlte,text='BLOOD GROUP :',font=("times new roman", 13)).grid(row=8,column=0)
            lab8=Label(dlte,text='COVID STATUS :',font=("times new roman", 13)).grid(row=9,column=0)
            lab9=Label(dlte,text='COVID VACCINATION STATUS :',font=("times new roman", 13)).grid(row=10,column=0)
            lab10=Label(dlte,text='PAST HISTORY :',font=("times new roman", 13)).grid(row=11,column=0)
            for i in range(1):
                p=list(data[i])
                name=(p[1])
                age=(p[2])
                gender=(p[3])
                date_of_birth=(p[4])
                height=(p[5])
                weight=(p[6])
                blood_group=(p[7])
                covid_status=(p[8])
                covid_vaccination_status=(p[9])
                past_history=(p[10])
            t='times new roman'
            e2=Label(dlte,text=name,font=(t,13)).grid(row=2,column=1)
            e3=Label(dlte,text=age,font=(t,13)).grid(row=3,column=1)
            e4=Label(dlte,text=gender,font=(t,13)).grid(row=4,column=1)
            e5=Label(dlte,text=date_of_birth,font=(t,13)).grid(row=5,column=1)
            e6=Label(dlte,text=height,font=(t,13)).grid(row=6,column=1)
            e7=Label(dlte,text=weight,font=(t,13)).grid(row=7,column=1)
            e8=Label(dlte,text=blood_group,font=(t,13)).grid(row=8,column=1)
            e9=Label(dlte,text=covid_status,font=(t,13)).grid(row=9,column=1)
            e10=Label(dlte,text=covid_vaccination_status,font=(t,13)).grid(row=10,column=1)
            e11=Label(dlte,text=past_history,font=(t,13)).grid(row=11,column=1)
            butn=Button(dlte,text='DELETE',command=dell,bg='light grey').grid(row=11,column=3)
        else:
            dlte.destroy()
            messagebox.showerror('OOPS','NO RECORD')
            
    def boom():
        dlte.destroy()
        
    btn=Button(dlte,text='EXIT',command=boom,bg='light grey').grid(row=11,column=2)

    def yo():
        try:
            a=e1.get()
            cursor.execute('Use test;')
            query='DELETE FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
            cursor.execute(query)
            data=cursor.fetchall()
            mydb.commit()
            dlte.destroy()
            messagebox.showinfo('SUCCESS','RECORD DELETED')
        except:
            messagebox.showerror('OOPS','NO RECORD')
            
    def dell():
        msg_box=tk.messagebox.askquestion('Delete Record','Are you sure you want to delete this record?',icon='warning')
        if msg_box=='yes':
            yo()
            try:
                dlte.destroy()
            except:
                pass
            


btn1=Button(text='ADD NEW RECORD',command=INSERT,bg='lavender').grid(row=1,column=0,padx=10,pady=5,ipadx=50)
btn2=Button(text='DISPLAY RECORD',command=view,bg='lavender').grid(row=2,column=0,padx=10,pady=5,ipadx=50)
btn3=Button(text='MODIFY RECORD',bg='lavender').grid(row=3,column=0,padx=10,pady=5,ipadx=50)
btn4=Button(text='DELETE RECORD',command=dlt,bg='lavender').grid(row=4,column=0,padx=10,pady=5,ipadx=50)
btn5=Button(text='EXIT',command=close1,bg='light grey').grid(row=5,column=0,pady=5,ipadx=25)

main_window.mainloop()
