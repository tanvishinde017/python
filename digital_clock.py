from tkinter import Tk
from tkinter import Label
import time

root=Tk()
root.title("clock")

def present_time():
    displaytime=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=displaytime)
    digi_clock.after(200,present_time)

def present_day():
    displaytime=time.strftime("%A")
    day.config(text=displaytime)
    day.after(100,present_time)


digi_clock=Label(root,font=("consolas",150), bg="black",fg="white")
digi_clock.pack()

day=Label(root,font=("Ink Free",150), bg="white",fg="black")
day.pack()

present_time()
present_day()


root.mainloop()
