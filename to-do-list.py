import tkinter as tk
from tkinter import messagebox


def add_task():
  task = task_entry.get()
  if task:
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)


def remove_task():
  selected_task = task_listbox.curselection()
  if selected_task:
    task_listbox.delete(selected_task)


def update_task():
  selected_task = task_listbox.curselection()
  if selected_task:
    new_task_description = task_entry.get()
    if new_task_description:
      task_listbox.delete(selected_task)
      task_listbox.insert(selected_task[0], new_task_description)
      task_entry.delete(0, tk.END)


def mark_as_completed():
  selected_task = task_listbox.curselection()
  if selected_task:
    task_index = selected_task[0]
    task_listbox.itemconfig(task_index, {'bg': 'light green'})
    task_entry.delete(0, tk.END)


def clear_completed():
  for i in reversed(range(task_listbox.size())):
    if task_listbox.itemcget(i, 'bg') == 'light green':
      task_listbox.delete(i)


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Remove Task Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Update Task Button
update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

# Mark as Completed Button
mark_button = tk.Button(root,
                        text="Mark as Completed",
                        command=mark_as_completed)
mark_button.pack()

# Clear Completed Button
clear_button = tk.Button(root, text="Clear Completed", command=clear_completed)
clear_button.pack()

# Task Listbox
task_listbox = tk.Listbox(root, width=40)
task_listbox.pack()

# Start the GUI main loop
root.mainloop()
