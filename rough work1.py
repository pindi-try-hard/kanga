import tkinter as tk
leftframeobjcol=tk()
def reset(flag=False):
   global checkvar4,checkvar3,checkvar2,checkvar1
   if flag:
    # 'No light' clicked
    if checkvar4.get():
      checkvar1.set(0)
      checkvar2.set(0)
      checkvar3.set(0)
   else:
    # other light clicked, reset 'No light' if any one of the others is checked
    checkvar4.set(0 if checkvar1.get() or checkvar2.get() or checkvar3.get() else 1)


   c1 = tk.Checkbutton(leftframeobjcol, text="UV", variable=checkvar1, command=reset)
   c1.pack(anchor="w")
   c2 = tk.Checkbutton(leftframeobjcol, text="Green", variable=checkvar2, command=reset)
   c2.pack(anchor="w")
   c3 = tk.Checkbutton(leftframeobjcol, text="Blue", variable=checkvar3, command=reset)
   c3.pack(anchor="w")
   c4 = tk.Checkbutton(leftframeobjcol, text="No light", variable = checkvar4, command=lambda:reset(True))
   c4.pack(anchor="w")
   leftframeobjcol.mainloop()