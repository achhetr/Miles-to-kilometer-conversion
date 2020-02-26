from tkinter import *

window = Tk()

def km_to_miles():
    try:
        km_to_miles = float(e1_var1.get()) * 1.6
    except ValueError:
        km_to_miles = "Not a Number!"
    
    t1.delete("1.0", END)
    t1.insert(END,km_to_miles)


b1 = Button(window,text="Press Me",command=km_to_miles)
b1.grid(row=0,column=0)

e1_var1 = StringVar()
e1 = Entry(window,textvariable=e1_var1)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()