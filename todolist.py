import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack the input field and buttons
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.RIGHT, padx=5)

# Create and pack the list view
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

# Start the main loop
root.mainloop()
