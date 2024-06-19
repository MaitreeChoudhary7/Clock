from tkinter import*
from tkinter.ttk import*
from time import strftime

root=Tk()
root.geometry("400x300")
root.title("clock")

def time():
    string=strftime("Clock \n%H \n%M \n%S")
    label.config(text=string)
    label.after(1,time)

label=Label(root,font=(" " ,40),background="black", foreground="white")
label.pack(anchor="center")
time()
mainloop()
