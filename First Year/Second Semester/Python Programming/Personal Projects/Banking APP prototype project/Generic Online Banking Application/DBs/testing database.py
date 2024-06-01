# # from sqlalchemy.dialects import mysql
# #
# # mydb = mysql.connect(
# #     host="bankdb@localhost",
# #     user="root",
# #     passwd="root",
# #     database = 'bankdb'
# # )
#
# #
# # from tkinter import *
# #
# # # Create object
# # root = Tk()
# #
# # # Adjust size
# # root.geometry("200x200")
# #
# #
# # # Change the label text
# # def show():
# #     label.config(text=clicked.get())
# #
# #
# # # Dropdown menu options
# # options = [
# #     "Monday",
# #     "Tuesday",
# #     "Wednesday",
# #     "Thursday",
# #     "Friday",
# #     "Saturday",
# #     "Sunday"
# # ]
# #
# # # datatype of menu text
# # clicked = StringVar()
# #
# # # initial menu text
# # clicked.set("Monday")
# #
# # # Create Dropdown menu
# # drop = OptionMenu(root, clicked, *options)
# # drop.pack()
# #
# # # Create button, it will change label text
# # button = Button(root, text="click Me", command=show).pack()
# #
# # # Create Label
# # label = Label(root, text=" ")
# # label.pack()
# #
# # # Execute tkinter
# # root.mainloop()
# #Import tkinter library
# from tkinter import *
# from tkinter import ttk
# #Create an instance of tkinter frame or window
# # win= Tk()
# # #Set the geometry of tkinter frame
# # win.geometry("750x250")
# # win.title("Main Window")
# # #Define a function to Open a new window
# # def open_win():
# #    child_win= Toplevel(win)
# #    child_win.title("Child Window")
# #    child_win.geometry("750x250")
# #    content= entry.get()
# #    Label(child_win, text=content, font=('Bell MT', 20, 'bold')).pack()
# #    win.withdraw()
# # #Create an Entry Widget
# # entry=ttk.Entry(win, width= 40)
# # entry.pack(ipady=4,pady=20)
# # #Let us create a button in the Main window
# # button= ttk.Button(win, text="OK",command=open_win)
# # button.pack(pady=20)
# # win.mainloop()
#
#
# import tkinter as tk
# from tkinter import ttk
#
#
# class ScrollableFrame(ttk.Frame):
#    def __init__(self, container, *args, **kwargs):
#       super().__init__(container, *args, **kwargs)
#
#       canvas = tk.Canvas(self)
#       scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
#       self.scroll = ttk.Frame(canvas)
#
#       self.scroll.bind(
#          "<Configure>",
#          lambda e: canvas.configure(
#             scrollregion=canvas.bbox("all")
#          )
#       )
#
#       canvas.create_window((0, 0), window=self.scroll, anchor="nw")
#
#       canvas.configure(yscrollcommand=scrollbar.set)
#
#       canvas.pack(side="left", fill="both", expand=True)
#       scrollbar.pack(side="right", fill="y")
#
#
# class App(tk.Tk):
#    def __init__(self):
#       super().__init__()
#
#       self.title("Scrollable Frame Example")
#       self.geometry("920x600")
#
#       container = ttk.Frame(self)
#       container.pack(fill="both", expand=True)
#
#       scrollable_frame = ScrollableFrame(container)
#       scrollable_frame.pack(fill="both", expand=True)
#
#       # Adding some example widgets to the scrollable frame
#       for i in range(50):
#          ttk.Label(scrollable_frame.scrollable_frame, text=f"Label {i}").pack()
#
#
# if __name__ == "__main__":
#    app = App()
#    app.mainloop()
#
