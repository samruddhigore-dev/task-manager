import tkinter as tk
from tkinter import messagebox
import sqlite3

# -DATABASE- #
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

# -FUNCTIONS- #

def format_task():
    task = entry.get().strip()
    priority = priority_var.get()
    deadline = deadline_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return None

    return f"{task} | {priority} | {deadline}"

def add_task():
    task_text = format_task()
    if task_text:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
        conn.commit()

        listbox.insert(tk.END, task_text)
        entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()

        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        listbox.delete(selected)

        if not task.startswith("✔ "):
            updated = "✔ " + task
        else:
            updated = task

        cursor.execute("UPDATE tasks SET task=? WHERE task=?", (updated, task))
        conn.commit()

        listbox.insert(selected, updated)
    except:
        messagebox.showwarning("Warning", "Select a task!")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        old_task = listbox.get(selected)

        new_task = format_task()
        if not new_task:
            return

        cursor.execute("UPDATE tasks SET task=? WHERE task=?", (new_task, old_task))
        conn.commit()

        listbox.delete(selected)
        listbox.insert(selected, new_task)

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

# Priority
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)

# Deadline
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

# ---------------- LOAD DATA ---------------- #
cursor.execute("SELECT task FROM tasks")
rows = cursor.fetchall()

for row in rows:
    listbox.insert(tk.END, row[0])

# Run app
root.mainloop()

# Close DB on exit
conn.close()