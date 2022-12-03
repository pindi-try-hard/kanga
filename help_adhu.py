from tkinter import *

win= Tk()
win.geometry("600x300")

label= Label(win, text= "Write something ??", font= ('comic san',20))
label.grid(row=1,column=0)
text= Text(win, height=10)
text.grid(row=2,column=0)

def delete():
   text.delete("1.0","end")
b1= Button(win, text= "Delete",command= delete)
b1.grid(row=3,column=0)
win.mainloop()
