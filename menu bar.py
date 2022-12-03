
from tkinter import *
window = Tk()
def show():
    print(clicked.get())
options = [
    "MALE",
    "FEMALE",
    "TRANSGENDER",
    "BISEXUAL",
    "Friday",
    "GAY",
    "LESBIAN"
]
clicked = StringVar()
clicked.set('choose your gender')
drop=OptionMenu(window,clicked,*options )
drop.pack()
button = Button(window,text = "click Me",command=show ).pack()
window.mainloop()
