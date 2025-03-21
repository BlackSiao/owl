import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

# 连接数据库
conn = sqlite3.connect("Daily.db")
cursor = conn.cursor()

# 确保任务表存在
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        priority TEXT NOT NULL CHECK(priority IN ('高', '中', '低'))
    )
''')
conn.commit()

# 显示任务列表
def show_tasks():
    task_listbox.delete(0, tk.END)  # 清空现有任务

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        task_listbox.insert(tk.END, f"{task[0]}. {task[1]} - {task[2]}")  # 格式化显示

# 添加新任务
def add_task():
    task_name = task_entry.get().strip()
    task_priority = priority_var.get()

    if not task_name:
        messagebox.showwarning("输入错误", "任务名称不能为空！")
        return

    cursor.execute("INSERT INTO tasks (name, priority) VALUES (?, ?)", (task_name, task_priority))
    conn.commit()
    show_tasks()  # 重新加载任务列表
    task_entry.delete(0, tk.END)  # 清空输入框

# 创建 GUI
root = tk.Tk()
root.title("RPG 任务栏")
root.geometry("600x400")

# 左侧任务栏
frame_left = tk.Frame(root, width=250, bg="#ddd")
frame_left.pack(side=tk.LEFT, fill=tk.Y)
task_listbox = tk.Listbox(frame_left)
task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 右侧任务管理
frame_right = tk.Frame(root, width=350, bg="#fff")
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

title_label = tk.Label(frame_right, text="📒 日常清单", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# 任务输入框
task_entry = tk.Entry(frame_right, width=30)
task_entry.pack(pady=5)

# 任务优先级选择
priority_var = tk.StringVar(value="中")
priority_menu = ttk.Combobox(frame_right, textvariable=priority_var, values=["高", "中", "低"], state="readonly")
priority_menu.pack(pady=5)

# 添加任务按钮
add_task_button = tk.Button(frame_right, text="添加任务", command=add_task, bg="green", fg="white")
add_task_button.pack(pady=10)

# 先加载任务
show_tasks()

# 运行 GUI
root.mainloop()

# 关闭数据库
conn.close()
