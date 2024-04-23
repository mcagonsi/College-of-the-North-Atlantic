import tkinter as tk
from tkinter import ttk as section

first = tk.Tk()
first.title("My Program")
first.geometry("640x720")

submitted = tk.Tk()
submitted.title('Success!')
submitted.geometry("300x300")


def submit():
    submitted.mainloop()
def cancel():
    submitted.destroy()
    first.destroy()

frame = section.Frame(first, padding='10 10 10 10')
frame.pack(fill='both',expand=True)
frame2 = section.Frame(submitted, padding='10 10 10 10')
frame2.pack(fill='both',expand=True)
exit = section.Button(submitted,text ='Exit', command = cancel)

button = section.Button(frame, text='submit',command= submit)
button2 = section.Button(frame,text='Cancel', command = cancel)
button.pack()
button2.pack()
exit.pack()

first.mainloop()