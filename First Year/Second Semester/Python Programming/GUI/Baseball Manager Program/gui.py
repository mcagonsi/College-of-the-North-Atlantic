import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db_functions
import objects

gui = tk.Tk()
gui.title("Baseball Manager - Player")
gui.geometry("400x600")
frame = ttk.Frame(gui, padding= '10 10 10 10')
frame.pack(fill='both', expand=True)

ID = ttk.Label(frame, text = 'Player ID: ')
ID.grid(row = 0, column = 0,sticky =tk.E)

ID = ttk.Label(frame, text = 'Player ID: ')
ID.grid(row = 1, column = 0,sticky =tk.E)

pos = ttk.Label(frame, text = 'Position: ')
pos.grid(row = 2, column = 0,sticky =tk.E)

atBats = ttk.Label(frame, text = 'At bats: ')
atBats.grid(row = 3, column = 0,sticky =tk.E)

hits = ttk.Label(frame, text = 'Hits: ')
hits.grid(row = 4, column = 0,sticky =tk.E)

batAvg = ttk.Label(frame, text = 'Batting Avg: ')
batAvg.grid(row = 5, column = 0,sticky =tk.E)