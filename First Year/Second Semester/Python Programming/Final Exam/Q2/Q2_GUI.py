
from tkinter import ttk
import pickle
import tkinter as tk
import Q2_functions as func


def readfile():  # handles the read file function
    try:
        with open('preferences.bin', 'rb') as pref:
            item = pickle.load(pref)
        preferences = item

        name.set(preferences.name)
        language.set(preferences.language)
        saveTime.set(preferences.saveTime)
    except FileNotFoundError:  # starts the program with default values if file not found
        Preferences.mainloop()


def writefile():
    Name = name.get()
    Language = language.get()
    SaveTime = saveTime.get()
    if Name == '':
        required = ttk.Label(Frame, text='Required')
        required.grid(row=0, column=4)

    elif SaveTime:
        try:
            SavedTime = int(SaveTime)
            file = func.Preferences(Name, Language, SavedTime)

            with open('preferences.bin', 'wb') as pref:
                pickle.dump(file, pref)
        except ValueError:
            Preferences.geometry('700x300')
            validMust = ttk.Label(Frame, text='Must be valid integer')
            validMust.grid(row=2, column=5)


# Preferences Window
Preferences = tk.Tk()
Preferences.title("Preferences")
Preferences.geometry("600x300")

# configure the frame
Frame = ttk.Frame(Preferences, padding='5 5 5 5')
Frame.pack(fill='both', expand=True)

# this is the Name label
nameLabel = ttk.Label(Frame, text='Name: ')
nameLabel.grid(column=0, row=0, sticky=tk.E, padx=0, pady=5)

# This is for the name entry field
name = tk.StringVar(value='')
nameEntry = ttk.Entry(Frame, width=40, textvariable=name)
nameEntry.grid(row=0, column=1, sticky=tk.W, columnspan=2, padx=0)

# this is for the language label
languageLabel = ttk.Label(Frame, text='Language: ')
languageLabel.grid(column=0, row=1, sticky=tk.E, padx=0)

# This is for the language entry field
language = tk.StringVar(value='English')
languageEntry = ttk.Entry(Frame, width=40, textvariable=language)
languageEntry.grid(row=1, column=1, sticky=tk.W, columnspan=2)

# this is for the time label
saveTimeLabel = ttk.Label(Frame, text='Auto Save Every X Minutes: ')
saveTimeLabel.grid(row=2, column=0, sticky=tk.E)

# this is for the time entry field
saveTime = tk.StringVar(value='0')
saveTimeEntry = ttk.Entry(Frame, width=40, textvariable=saveTime)
saveTimeEntry.grid(row=2, column=1, sticky=tk.W, columnspan=2)

# save button
saveButton = ttk.Button(Frame, text='Save', width=15, command=writefile)
saveButton.grid(row=3, column=1)

# cancel button
cancelButton = ttk.Button(Frame, text='Cancel', width=15, command=quit)
cancelButton.grid(row=3, column=2)

# configures padding for the components
for child in Frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# reads the file first
readfile()

# starts the GUI
Preferences.mainloop()
