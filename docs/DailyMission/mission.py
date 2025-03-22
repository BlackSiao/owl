import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# 连接数据库
conn = sqlite3.connect("Daily.db")
cursor = conn.cursor()

# 获取今天的日期并创建表名
today = datetime.today().strftime('%Y_%m_%d')

# 确保任务表存在
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS "{today}" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        priority TEXT NOT NULL CHECK(priority IN ('高', '中', '低')),
        completed INTEGER DEFAULT 0
    )
''')
conn.commit()

# 添加新任务
def add_task():
    task_name = task_entry.get()
    task_priority = priority_var.get()

    if not task_name:
        messagebox.showwarning("输入错误", "任务名称不能为空！")
        return

    cursor.execute(f'INSERT INTO "{today}" (name, priority) VALUES (?, ?)', (task_name, task_priority))
    conn.commit()
    task_entry.delete(0, tk.END)
    show_tasks()

# 标记任务为完成
def complete_task(task_id):
    cursor.execute(f'UPDATE "{today}" SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    show_tasks()

# 显示任务（使用 Treeview）
def show_tasks():
    for item in task_tree.get_children():
        task_tree.delete(item)

    cursor.execute(f'SELECT id, name, priority, completed FROM "{today}" ORDER BY completed, priority')
    tasks = cursor.fetchall()

    for task in tasks:
        task_id, task_name, task_priority, completed = task
        status = "✔️ 已完成" if completed else "❌ 未完成"
        
        # 插入任务
        task_tree.insert("", "end", values=(task_id, task_name, task_priority, status), tags=("completed" if completed else "pending"))

    # 配置已完成任务的划线效果
    task_tree.tag_configure("completed", foreground="gray", font=("Arial", 12, "overstrike"))
    task_tree.tag_configure("pending", font=("Arial", 12))

# 创建 GUI
root = tk.Tk()
root.title("日常清单")
root.geometry("700x450")
root.configure(bg="#f4f4f4")

# **任务输入框**
task_frame = tk.Frame(root, bg="#f4f4f4")
task_frame.pack(pady=10)

tk.Label(task_frame, text="任务名称:", font=("Arial", 13), bg="#f4f4f4").grid(row=0, column=0, padx=5)
task_entry = tk.Entry(task_frame, width=30, font=("Arial", 13))
task_entry.grid(row=0, column=1, padx=5)

tk.Label(task_frame, text="优先级:", font=("Arial", 13), bg="#f4f4f4").grid(row=0, column=2, padx=5)
priority_var = tk.StringVar(value="中")
priority_menu = ttk.Combobox(task_frame, textvariable=priority_var, values=["高", "中", "低"], state="readonly", width=8, font=("Arial", 12))
priority_menu.grid(row=0, column=3, padx=5)

add_task_button = tk.Button(task_frame, text="添加任务", command=add_task, bg="green", fg="white", font=("Arial", 13, "bold"), width=10)
add_task_button.grid(row=0, column=4, padx=5)

# **任务显示框 (Treeview)**
columns = ("ID", "任务名称", "优先级", "状态")
task_tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
task_tree.heading("ID", text="ID")
task_tree.heading("任务名称", text="任务名称")
task_tree.heading("优先级", text="优先级")
task_tree.heading("状态", text="状态")

task_tree.column("ID", width=50, anchor="center")
task_tree.column("任务名称", width=300)
task_tree.column("优先级", width=100, anchor="center")
task_tree.column("状态", width=100, anchor="center")

task_tree.pack(pady=10)

# **完成任务按钮**
def mark_completed():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showwarning("提示", "请先选择要完成的任务！")
        return

    task_id = task_tree.item(selected_item, "values")[0]
    complete_task(task_id)

complete_task_button = tk.Button(root, text="标记为完成", command=mark_completed, bg="blue", fg="white", font=("Arial", 13, "bold"), width=12)
complete_task_button.pack(pady=5)

# 加载任务列表
show_tasks()

# 运行 GUI
root.mainloop()

# 关闭数据库
conn.close()
