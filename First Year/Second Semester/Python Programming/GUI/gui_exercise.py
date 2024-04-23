import tkinter as tk
from tkinter import ttk as section

first = tk.Tk()
first.title("My Program")
first.geometry("400x400")
frame = section.Frame(first, padding='10 10 10 10')
frame.pack(fill='both',expand=True)



def submit():
    name = name_text.get()
    about_text.set(f'{name} is freaking awesome')
def cancel():

    first.destroy()


name_label = section.Label(frame, text = 'Name: ')
name_label.grid(row = 0, column = 0,sticky =tk.E)
# name_label.pack()
name_text = tk.StringVar()
name_entry = section.Entry(frame, width=50, textvariable=name_text)
name_entry.grid(row = 0, column =1)
# name_entry.pack()
about_label = section.Label(frame, text = 'About: ')
about_label.grid(row = 1, column = 0, sticky=tk.E)
# about_label.pack()
about_text = tk.StringVar()
about_entry = section.Entry(frame, width = 50, textvariable=about_text, state='readonly')
about_entry.grid(row = 1, column =1)
# about_entry.pack()
button = section.Button(frame, text='submit',command= submit)
button.grid(row = 3, column = 0)
button2 = section.Button(frame,text='Cancel', command = cancel)
button2.grid(row = 3, column = 1)

# button.pack()
# button2.pack()


first.mainloop()