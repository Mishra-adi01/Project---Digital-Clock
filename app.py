import tkinter as tk # tkinter module use to build GUI in python 
from time import strftime

# creating object named root with the help of tkinter class
root = tk.Tk()
root.title("Digital Clock") # Set the title

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

# creating object named label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='#bfd7ea', foreground='#014d4e')
label.pack(anchor='center')

time()
root.mainloop()