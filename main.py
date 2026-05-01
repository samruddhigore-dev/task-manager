import tkinter as tk
from tkinter import messagebox

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

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

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")
root.resizable(False, False)

# Dark theme background
root.configure(bg="#1e1e2f")

# Title
tk.Label(
    root,
    text="My Task Manager",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=10)

# Input field
entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    bg="#2e2e3f",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=10)

# Buttons
tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task,
    bg="#05510A",
    fg="white"
).pack(pady=5)

tk.Button(
    root,
    text="Delete Task",
    width=20,
    command=delete_task,
    bg="#B11010",
    fg="white"
).pack(pady=5)

tk.Button(
    root,
    text="Mark Completed",
    width=20,
    command=mark_complete,
    bg="#A164AA",
    fg="white"
).pack(pady=5)

# Task list
listbox = tk.Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 11),
    bg="#2e2e3f",
    fg="white",
    selectbackground="#6a5acd"
)
listbox.pack(pady=20)

# Run app
root.mainloop()