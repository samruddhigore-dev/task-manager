import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = entry.get().strip()
    priority = priority_var.get()
    deadline = deadline_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    task_text = f"{task} | {priority} | {deadline}"
    listbox.insert(tk.END, task_text)

    entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)

        if not task.startswith("✔ "):
            listbox.insert(tk.END, "✔ " + task)
        else:
            listbox.insert(tk.END, task)

    except:
        messagebox.showwarning("Warning", "Select a task!")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get().strip()

        if new_task == "":
            messagebox.showwarning("Warning", "Enter new task!")
            return

        priority = priority_var.get()
        deadline = deadline_entry.get().strip()

        updated = f"{new_task} | {priority} | {deadline}"

        listbox.delete(selected)
        listbox.insert(selected, updated)

        entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

    except:
        messagebox.showwarning("Warning", "Select a task to edit!")

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Task Manager")
root.geometry("450x600")
root.resizable(False, False)

root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="Task Manager",
         font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Task input
entry = tk.Entry(root, width=35, font=("Arial", 12),
                 bg="#2e2e3f", fg="white", insertbackground="white")
entry.pack(pady=5)

# Priority dropdown
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)

# Deadline input
deadline_entry = tk.Entry(root, width=35, font=("Arial", 12))
deadline_entry.insert(0, "Deadline (YYYY-MM-DD)")
deadline_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Add Task", width=20, command=add_task,
          bg="#4CAF50", fg="white").pack(pady=5)

tk.Button(root, text="Delete Task", width=20, command=delete_task,
          bg="#f44336", fg="white").pack(pady=5)

tk.Button(root, text="Mark Completed", width=20, command=mark_complete,
          bg="#2196F3", fg="white").pack(pady=5)

tk.Button(root, text="Edit Task", width=20, command=edit_task,
          bg="#ff9800", fg="white").pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=15,
                     font=("Arial", 11),
                     bg="#2e2e3f", fg="white",
                     selectbackground="#6a5acd")
listbox.pack(pady=20)

root.mainloop()