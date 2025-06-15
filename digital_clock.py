from tkinter import Tk
from tkinter import Label
import time

root=Tk()
root.title("clock")

def present_time():
    displaytime=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=displaytime)
    digi_clock.after(200,present_time)



digi_clock=Label(root,font=("arial",150), bg="black",fg="white")
digi_clock.pack()

present_time()

root.mainloop()