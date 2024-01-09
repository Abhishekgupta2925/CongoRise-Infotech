import tkinter as tk

def on_click(button_value):
    current = entry_var.get()
    entry_var.set(current + str(button_value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the current expression
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Helvetica", 14))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear and calculate buttons
tk.Button(root, text="C", padx=20, pady=20, command=clear_entry).grid(row=5, column=0)
tk.Button(root, text="=", padx=20, pady=20, command=calculate).grid(row=5, column=1, columnspan=3)

# Run the application
root.mainloop()
