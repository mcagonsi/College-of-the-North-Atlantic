import locale as lc
import tkinter as tk
from tkinter import ttk, messagebox


def futureValue(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest

    lc.setlocale(lc.LC_ALL, 'en_US')

    future_value_calc = lc.currency(future_value, grouping=True)
    return future_value_calc


def cal():
    def submit():
        mon_inv = monthly_investment.get()
        year_int = yearly_interest.get()
        Years = years.get()
        if mon_inv == 0 or year_int == 0 or Years == 0:
            messagebox.showerror(title='Error', message='Value must be greater than 0')
        elif isinstance(mon_inv, str) or isinstance(year_int, str) or isinstance(Years, str):
            messagebox.showinfo(title='Error', message='Text not allowed only numbers')
        else:
            future_value = futureValue(mon_inv, year_int, Years)
            Futurevalue_output.set(f'{future_value}')

    Calculator = tk.Tk()
    Calculator.title('Future Value Calculator')
    Calculator.geometry('500x500')

    Window = ttk.Frame(Calculator, padding='10 10 10 10')
    Window.pack(fill='both', expand=True)
    monthly_investment_label = ttk.Label(Window, text='Enter monthly investment:\t\t')
    monthly_investment_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

    monthly_investment = tk.IntVar(value=0)
    monthly_investment_entry = ttk.Entry(Window, width=40, textvariable=monthly_investment)
    monthly_investment_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

    yearly_interest_label = ttk.Label(Window, text='Enter yearly interest:\t\t')
    yearly_interest_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

    yearly_interest = tk.IntVar(value=0)
    yearly_interest_entry = ttk.Entry(Window, width=40, textvariable=yearly_interest)
    yearly_interest_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

    years_label = ttk.Label(Window, text='Enter number of years:\t\t ')
    years_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

    years = tk.IntVar(value=0)
    years_entry = ttk.Entry(Window, width=40, textvariable=years)
    years_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

    Futurevalue = ttk.Label(Window, text='Future value: ')
    Futurevalue.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)

    Futurevalue_output = tk.StringVar()
    futurevalue_output = ttk.Entry(Window, width=40, textvariable=Futurevalue_output, state='readonly')
    futurevalue_output.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

    cancel = ttk.Button(Window, width=20, text='Cancel', command=Window.quit)
    cancel.grid(row=5, column=0, sticky=tk.S, padx=10, pady=10)

    Submit = ttk.Button(Window, width=20, text='Submit', command=submit)
    Submit.grid(row=5, column=1, sticky=tk.S, padx=10, pady=10)

    Window.mainloop()


def main():
    cal()


if __name__ == '__main__':
    main()
