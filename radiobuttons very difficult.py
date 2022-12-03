'''from tkinter import *
window = Tk()
mode_of_transportation = Label(window, text="Mode of transportation: ")
mode_of_transportation.grid(column=1, row=1)
r = StringVar()
express = Radiobutton(text="Express(Grab,Uber,Taxi)",variable=r,value=0,highlightthickness=0)
express.grid(column=1, row=2, sticky="W")
normal = Radiobutton(text="Normal(Jeep,Bus,UV,Tric)",variable=r,value=1,highlightthickness=0)
normal.grid(column=1, row=3, sticky="W")
print(r.get())
window.mainloop()

from tkinter import *

window = Tk()
mimeType = StringVar()  # is a string variable but in the original code mimeType was being set an object.
mimeType.set('Initialize')  # So the later print statement will print something

# original code value = was being set to objects.
wave = StringVar(value="audio/wav")  # These are objects no longer needed?
mp3 = StringVar(value='audio/mp3')  # These are objects no longer needed?
mp4 = StringVar(value='audio/mp4')  # These are objects no longer needed?
mp2 = StringVar(value='audio/mp2')  # These are objects no longer needed?
flac = StringVar(value='audio/flac')  # These are objects no longer needed?
m4a = StringVar(value='audio/m4a')  # These are objects no longer needed?
def display_current_mimetype():
    print(mimeType.get())
Radiobutton(window, text="MP3 Format", variable=mimeType,value='audio/mp3',command=display_current_mimetype).pack(anchor=W)

Radiobutton(window, text="MP4 Format", variable=mimeType,
            height=5,
            width=20, value='audio/mp4', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype).pack(
    anchor=W)

Radiobutton(window, text="MP2 Format", variable=mimeType,
            height=5,
            width=20, value='audio/mp2', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype).pack(
    anchor=W)
Radiobutton(window, text="WAV Format", variable=mimeType,
            height=5,
            width=20, value="audio/wav", bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype).pack(
    anchor=W)
Radiobutton(window, text="M4A Format", variable=mimeType,
            height=5,
            width=20, value='audio/m4a', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype).pack(
    anchor=W)

print(mimeType.get())  # Will print the initial value

mainloop()'''

#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter Frame
win.geometry("750x250")

#Add a Top widget
Label(win,text= "Select an Option from the Menu", font=('Aerial', 15, 'bold')).pack(pady=15)

#Define CheckButtons
option_dict={}
values=["C++", "Python", "JavaScript", "Ruby","GoLang"]
for i in values:
   cb= ttk.Checkbutton(win, text=i,state= "disabled")
   cb.pack()
#Create a Button widget
win.mainloop()