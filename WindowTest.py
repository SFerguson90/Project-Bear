import tkinter as tk
from tkinter import ttk

## ROOT WINDOW TITLE & INITIALIZATION

root = tk.Tk()
root.title("Bear Program Test")

## VALUES

stock_value = tk.StringVar()
start_date_value = tk.StringVar()
end_date_value = tk.StringVar()

## WINDOW BASICS & GRID STYLE

main = ttk.Frame(root, padding=(30,15))
main.grid()

## CREATING LABELS / INPUTS / BUTTONS

stock_label = ttk.Label(main, text='Stock:')
stock_input = ttk.Entry(main, width=10, textvariable=stock_value)
start_date_label = ttk.Label(main, text='Start Date:')
start_date_input = ttk.Entry(main, width=10, textvariable=start_date_value)
end_date_label = ttk.Label(main, text='End Date:')
end_date_input = ttk.Entry(main, width=10, textvariable=end_date_value)
calc_button = ttk.Button(main, text='Calculate')

## PLACING LABELS / INPUTS / BUTTONS

stock_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
stock_input.grid(column=1, row=0, sticky='EW', padx=5, pady=5)
stock_input.focus()

start_date_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
start_date_input.grid(column=1, row=1, sticky='EW', padx=5, pady=5)

end_date_label.grid(column=0, row=2, sticky="W", padx=5, pady=5)
end_date_input.grid(column=1, row=2, sticky='EW', padx=5, pady=5)

calc_button.grid(column=0, row=3, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()
