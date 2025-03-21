import tkinter as tk
import sqlite3
from tkinter import ttk

# 创建/连接数据库
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# 创建任务表（如果不存在）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        name TEXT NOT NULL,
        deadline TEXT NOT NULL
    )
''')
conn.commit()

# 预填充示例任务（仅执行一次）
sample_tasks = [
    ("日常清单", "吃饭", "12:00"),
    ("日常清单", "学习 Python", "14:00"),
    ("主线任务", "击败Boss", "2025-03-30"),
    ("支线任务", "收集5个金币", "2025-03-22"),
    ("已归档任务", "完成新手教程", "2025-03-10")
]

# 检查是否已填充数据
cursor.execute("SELECT COUNT(*) FROM tasks")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO tasks (category, name, deadline) VALUES (?, ?, ?)", sample_tasks)
    conn.commit()

conn.close()  # 关闭数据库连接

# 任务管理界面
root = tk.Tk()
root.title("RPG 任务栏")
root.geometry("600x400")

# 任务类别
categories = ["日常清单", "主线任务", "支线任务", "已归档任务"]
selected_option = tk.StringVar(root)
selected_option.set(categories[0])  # 默认选择第一个类别

# 任务列表框
task_listbox = tk.Listbox(root)
task_listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# **查询并显示任务**
def ShowTask(selected_category):
    task_listbox.delete(0, tk.END)  # 清空列表

    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, deadline FROM tasks WHERE category = ?", (selected_category,))
    tasks = cursor.fetchall()
    
    conn.close()

    # 将查询到的任务添加到任务列表框
    for name, deadline in tasks:
        task_listbox.insert(tk.END, f"{name} - 截止: {deadline}")

# 显示任务列表
def ShowTask(selected_category):
    # 清空左侧任务列表
    task_listbox.delete(0, tk.END)

    # 获取当前选择的任务数据
    tasks = task_data.get(selected_category, [])
    
    # 显示任务到左侧面板
    for task_name, task_deadline in tasks:
        task_listbox.insert(tk.END, f"{task_name} - 截止: {task_deadline}")

# 开始进行页面布局
root = tk.Tk()
root.title("RPG 任务栏")
root.geometry("600x400")

# 设置下拉菜单
categories = ["日常清单", "主线任务", "支线任务", "已归档任务"]

# 创建StringVar对象
selected_option = tk.StringVar(root)
selected_option.set(categories[0])

# 创建选项菜单对象（command 传函数名，不要加括号）
option_menu = tk.OptionMenu(root, selected_option, *categories, command=ShowTask)
option_menu.pack(side=tk.TOP, fill=tk.X, padx=200)

# 设置页面左边栏
frame_left = tk.Frame(root, width=200, bg="#ddd")
frame_left.pack(side=tk.LEFT, fill=tk.Y)

# 创建 Listbox 来显示任务
task_listbox = tk.Listbox(frame_left)
task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 设置页面右边栏
frame_right = tk.Frame(root, width=400, bg="#fff")
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# 先显示默认的“日常清单”任务
ShowTask(categories[0])

# 运行主循环s
root.mainloop()
