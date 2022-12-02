from tkinter import *
from tkinter import messagebox
main_window=Tk()
main_window.geometry('240x200')
#main_window.config(bg='lig')
main_window.title('HOMEPAGE')

global admn
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger')
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
        NAME CHAR(130) NOT NULL,
        AGE INT,
        SEX CHAR(130),
        HEIGHT INT,
        WEIGHT INT,
        BLOOD_GROUP CHAR(130),
        COVID_VACCINATION CHAR(130),
        COVID_VACCINATION_DETAILS CHAR(130),
        PRE_MEDICAL_HISTORY CHAR(130))''')
        cursor.execute(sql)
    except mysql.connector.errors.ProgrammingError :
        
        break
cursor.execute("use test")
def INSERT():
    global new_window,ent1,ent2,ent3,ent5,ent6,ent7,clicked1,clicked
    new_window=Toplevel(main_window)
    #new_window=Tk()
    new_window.title("ENTER RECORDS")
    #new_window.config(background='')
    lab1=Label(new_window,text='ADMN NUMBER',font=("times new roman", 13)).grid(row=1,column=0)
    lab2=Label(new_window,text='NAME',font=("times new roman", 13)).grid(row=2,column=0)
    lab3=Label(new_window,text='AGE',font=("times new roman", 13)).grid(row=3,column=0)
    lab4=Label(new_window,text='GENDER',font=("times new roman", 13)).grid(row=4,column=0)
    lab5=Label(new_window,text='DOB',font=('times new roman',13)).grid(row=5,column=0)
    lab6=Label(new_window,text='HEIGHT(in cms)',font=("times new roman", 13)).grid(row=6,column=0)
    lab7=Label(new_window,text='WEIGHT(in kg)',font=("times new roman", 13)).grid(row=7,column=0)
    lab8=Label(new_window,text='BLOOD GROUP',font=("times new roman", 13)).grid(row=8,column=0)
    lab9=Label(new_window,text='COVID STATUS',font=("times new roman", 13)).grid(row=9,column=0)
    lab10=Label(new_window,text='COVID VACCINATION STATUS',font=("times new roman", 13)).grid(row=10,column=0)
    lab11=Label(new_window,text='Past History',font=("times new roman", 13)).grid(row=11,column=0)
    lab12=Label(new_window,text='').grid(row=12,column=0)
    lab13=Label(new_window,text='Any major illness/operations in past',font=("times new roman", 12)).grid(row=13,column=0,padx=100)
    lab14=Label(new_window,text='Using any implant/accessories',font=('times new roman',12)).grid(row=14,column=0)
    ent1=Entry(new_window)
    ent1.grid(row=1,column=1,)
    ent2=Entry(new_window)
    ent2.grid(row=2,column=1)
    ent3=Entry(new_window)
    ent3.grid(row=3,column=1)
    #ent5=Entry(new_window)
    #ent5.grid(row=5,column=1)
    ent6=Entry(new_window)
    ent6.grid(row=6,column=1)
    ent7=Entry(new_window)
    ent7.grid(row=7,column=1)
    #ent7=Entry(new_window)
    #ent7.grid(row=7,column=1)
    #ent8=Entry(new_window)
    #ent8.grid(row=8,column=1)
    #ent9=Entry(new_window)
    #ent9.grid(row=9,column=1)
    #ent10=Entry(new_window)
    #ent10.grid(row=10,column=1)
    ent11=Entry(new_window)
    ent11.grid(row=13,column=1)
    t1 = Checkbutton(new_window, text="Jaundice", variable=var1, onvalue='Jaundice', offvalue='')
    t1.grid(sticky='W',row=11,column=1)
    t2 = Checkbutton(new_window, text="Allergies", variable=var2, onvalue='Allergies', offvalue='')
    t2.grid(sticky='W',row=11,column=2)
    t3 = Checkbutton(new_window, text="Blood Transfusion", variable=var3, onvalue='Blood Transfusion', offvalue='')
    t3.grid(sticky='W',row=12,column=1)
    t4 = Checkbutton(new_window, text="Dental implant", variable=var4, onvalue='Dental implant', offvalue='')
    t4.grid(sticky='W',row=14,column=1)
    t5 = Checkbutton(new_window, text='Braces', variable=var5, onvalue='Braces', offvalue='')
    t5.grid(sticky='W',row=14,column=2)
    t6 = Checkbutton(new_window, text="Spectacles", variable=var6, onvalue='Spectacles', offvalue='')
    t6.grid(sticky='W',row=15,column=1)
    t9 = Checkbutton(new_window, text="NIL", variable=var9, onvalue='NIL', offvalue='')
    YES = Radiobutton(new_window,text="YES",variable=f,value='YES',command=vaccine())
    YES.grid(row=10,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=f,value='NO',command=vaccine())
    NO.grid(row=10,column=2,sticky="W")
    t9.grid(sticky='W',row=12,column=2)
    YES = Radiobutton(new_window,text="YES",variable=r,value='YES',command=COVID())
    YES.grid(row=9,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=r,value='NO',command=COVID())
    NO.grid(row=9,column=2,sticky="W")
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
    clicked1.set('BLOOD GROUP')
    drop=OptionMenu(new_window,clicked1,*options)
    drop.grid(row=8,column=1)
    options = [
    "Male",
    "Female",
    "Other"
    ]
    clicked = StringVar()
    clicked.set('M/F/O')
    drop=OptionMenu(new_window,clicked,*options )
    drop.grid(row=4,column=1)

    date=[1,2,3,4,5,6,7,8,9,10,11,12,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    months=['January','February','March','April','May','June','July','August','September','October',
    'Novermber','December']
    year=[]
    for i in range(1940,2050):
        year.append(i)
    
    clicked3=StringVar()
    clicked3.set('Month')
    clicked2=IntVar()
    clicked2.set('Date')
    clicked4=IntVar()
    clicked4.set('Year')
    drop=OptionMenu(new_window,clicked4,*year)
    drop.grid(row=5,column=3)
    drop=OptionMenu(new_window,clicked3,*months)
    drop.grid(sticky='W',row=5,column=2)
    drop=OptionMenu(new_window,clicked2,*date)
    drop.grid(sticky='W',row=5,column=1)
    btn=Button(new_window,text="ENTER",command=savedata,bg='light grey')
    btn.grid(row=20,column=2)
    
    bmbtn=Button(new_window,text='FIND bmi',command=BMI,bg='light grey')
    bmbtn.grid(row=20,column=1)
    btnquit=Button(new_window,text='Exit',command=close,bg='light grey')
    btnquit.grid(row=20,column=3)

admn=IntVar()
def view():
    global admn
    import tkinter as tk
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tiger')
    cursor = mydb.cursor()
    view=tk.Tk()
    view.title('Details')
    view.geometry('500x300')
    lab1=Label(view,text='ADMN NUMBER :',font=("times new roman", 13)).grid(row=1,column=0)
    e1=Entry(view,textvariable=admn)
    e1.grid(row=1,column=1)
    adm=e1.get()
    
    
    def disp():
        
        lab2=Label(view,text='NAME :',font=("times new roman", 13)).grid(row=2,column=0)
        lab3=Label(view,text='AGE :',font=("times new roman", 13)).grid(row=3,column=0)
        lab4=Label(view,text='GENDER :',font=("times new roman", 13)).grid(row=4,column=0)
        lab5=Label(view,text='HEIGHT(cm) :',font=("times new roman", 13)).grid(row=5,column=0)
        lab6=Label(view,text='WEIGHT(kg) :',font=("times new roman", 13)).grid(row=6,column=0)
        lab7=Label(view,text='BLOOD GROUP :',font=("times new roman", 13)).grid(row=7,column=0)
        lab8=Label(view,text='COVID STATUS :',font=("times new roman", 13)).grid(row=8,column=0)
        lab9=Label(view,text='COVID VACCINATION STATUS :',font=("times new roman", 13)).grid(row=9,column=0)
        lab10=Label(view,text='PAST HISTORY :',font=("times new roman", 13)).grid(row=10,column=0)
        cursor.execute('Use test;')
        print(adm)
        '''query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(adm)
        cursor.execute(query)
        data=cursor.fetchall()
        mydb.commit()

        for i in range(1):
            p=list(data[i])
            admn=(p[0])
            name=(p[1])
            age=(p[2])
            gender=(p[3])
            height=(p[4])
            weight=(p[5])
            bld_grp=(p[6])
            covid=(p[7])
            vaccine=(p[8])
            past=(p[9])'''

        e2=Label(view,text=name,font=("times new roman", 13)).grid(row=2,column=1)
        e3=Label(view,text=age,font=("times new roman", 13)).grid(row=3,column=1)
        e4=Label(view,text=gender,font=("times new roman", 13)).grid(row=4,column=1)
        e5=Label(view,text=height,font=("times new roman", 13)).grid(row=5,column=1)
        e6=Label(view,text=weight,font=("times new roman", 13)).grid(row=6,column=1)
        e7=Label(view,text=bld_grp,font=("times new roman", 13)).grid(row=7,column=1)
        e8=Label(view,text=covid,font=("times new roman", 13)).grid(row=8,column=1)
        e9=Label(view,text=vaccine,font=("times new roman", 13)).grid(row=9,column=1)
        e10=Label(view,text=past,font=("times new roman", 13)).grid(row=10,column=1)
    btn9=Button(view,text='VIEW',command=disp,bg='light grey')
    btn9.grid(row=1,column=2)
    
    
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


def viewlay_input():
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
    age=ent3.get()
    sex=show()
    height=ent6.get()
    weight=ent7.get()
    blood_group=blood_GROUP()
    covid_vaccination=COVID()
    covid_vaccination_details=vaccine()
    pre_medical_history=viewlay_input()
    try:
        
        cursor.execute('''insert into medical_records
         (admn_number,name,age,sex,height,weight,blood_group,covid_vaccination,
         covid_vaccination_details,pre_medical_history)'''
         "values('"+admn_number+"','"+name+"','"+age+"','"+sex+"','"+height+"','"+weight+"','"+blood_group+"','"+covid_vaccination+"','"+covid_vaccination_details+"','"+pre_medical_history+"')")
        messagebox.showinfo('Success','Record inserted')
    except:
        messagebox.showinfo('Utter failure','Record already exists')

    mydb.commit()
        



btn6=Button(text='ADD NEW RECORD',command=INSERT,bg='lavender').grid(row=1,column=0,padx=10,pady=5,ipadx=50)
btn8=Button(text='DISPLAY RECORD',command=view,bg='lavender').grid(row=2,column=0,padx=10,pady=5,ipadx=50)
btn8=Button(text='MODIFY RECORD',bg='lavender').grid(row=3,column=0,padx=10,pady=5,ipadx=50)
btn8=Button(text='DELETE RECORD',command=close,bg='lavender').grid(row=4,column=0,padx=10,pady=5,ipadx=50)
btn7=Button(text='EXIT',command=close1,bg='light grey').grid(row=5,column=0,pady=5,ipadx=25)



main_window.mainloop()
