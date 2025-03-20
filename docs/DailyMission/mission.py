import tkinter as tk
from tkinter import ttk

def show_task_details(event):
    selected_item = task_list.focus()
    if selected_item:
        details_var.set(task_data.get(selected_item, "No details available"))

def add_task():
    new_task = entry_task.get()
    if new_task:
        category = category_var.get()
        if category:
            item_id = task_views[category].insert("", "end", text=new_task)
            task_data[item_id] = "Task Details: " + new_task  # 临时存储任务详情
            entry_task.delete(0, tk.END)

def archive_task():
    selected_item = task_list.focus()
    if selected_item:
        archived_tasks.insert("", "end", text=task_list.item(selected_item, "text"))
        task_list.delete(selected_item)

def toggle_visibility(category):
    if treeview_states[category].get():
        task_views[category].pack(fill=tk.BOTH, expand=True)
    else:
        task_views[category].pack_forget()

task_data = {}

treeview_states = {}
task_views = {}

# 开始进行页面布局
root = tk.Tk()
root.title("RPG 任务管理系统")
root.geometry("600x400")
# 设置页面左边栏
frame_left = tk.Frame(root, width=200, bg="#ddd")
frame_left.pack(side=tk.LEFT, fill=tk.Y)
# 设置页面右边栏
frame_right = tk.Frame(root, width=400, bg="#fff")
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# 设置主要内容
categories = ["主线任务", "支线任务", "日常清单", "已归档任务"]
for cat in categories:
    # 创建一个BooleanVar变量来控制类别的显示状态
    treeview_states[cat] = tk.BooleanVar(value=True)
    # 创建一个新的fram,水平的填充到左边栏
    frame_cat = tk.Frame(frame_left, bg="#ddd")
    frame_cat.pack(fill=tk.X)
    # 设置复选按钮，实现下拉菜单的功能
    toggle_btn = tk.Checkbutton(
        frame_cat, 
        text=cat,
        bg="#ddd", 
        font=("Arial", 12, "bold"), 
        variable=treeview_states[cat], 
        command=lambda c=cat: toggle_visibility(c))
    toggle_btn.pack(side=tk.LEFT, anchor="w")
    
    task_views[cat] = ttk.Treeview(frame_left)
    task_views[cat].pack(fill=tk.BOTH, expand=True)

task_list = ttk.Treeview(frame_left)
task_list.pack(fill=tk.BOTH, expand=True)
task_list.bind("<Motion>", show_task_details)

details_var = tk.StringVar()
details_label = tk.Label(frame_right, textvariable=details_var, wraplength=350, justify="left", bg="#fff")
details_label.pack(pady=20)

entry_task = tk.Entry(frame_left)
entry_task.pack(fill=tk.X)
category_var = tk.StringVar(value="主线任务")
category_menu = ttk.Combobox(frame_left, textvariable=category_var, values=categories)
category_menu.pack(fill=tk.X)
btn_add = tk.Button(frame_left, text="添加任务", command=add_task)
btn_add.pack(fill=tk.X)
btn_archive = tk.Button(frame_left, text="归档任务", command=archive_task)
btn_archive.pack(fill=tk.X)

archived_tasks = ttk.Treeview(frame_left)
archived_tasks.pack(fill=tk.BOTH, expand=True)

root.mainloop()
