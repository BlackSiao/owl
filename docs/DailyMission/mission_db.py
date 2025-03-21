import sqlite3
from datetime import datetime

# 连接数据库
conn = sqlite3.connect("Daily.db")
cursor = conn.cursor()

# 获取当天日期（格式：YYYY-MM-DD）
today = datetime.today().strftime('%Y-%m-%d')

# **改进点 1：添加 `date` 字段**
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        priority TEXT NOT NULL CHECK(priority IN ('高', '中', '低')),
        date TEXT NOT NULL  -- 新增：记录任务日期
    )
''')
conn.commit()

# **改进点 2：加载当天任务**
def get_today_tasks():
    cursor.execute("SELECT * FROM tasks WHERE date = ?", (today,))
    return cursor.fetchall()

# **改进点 3：添加任务时防止重复**
def add_task(name, priority):
    # 检查今天是否已经有相同任务
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE name = ? AND date = ?", (name, today))
    if cursor.fetchone()[0] > 0:
        print(f"任务 '{name}' 已存在于今天的清单中，跳过插入。")
        return

    # 插入新任务
    cursor.execute("INSERT INTO tasks (name, priority, date) VALUES (?, ?, ?)", (name, priority, today))
    conn.commit()

# **测试插入任务**
sample_tasks = [
    ("学习 Shell 脚本", "高"),
    ("复习数据结构与算法", "中"),
    ("完成 Python 练习项目", "高"),
    ("投递深圳的开发工程师职位", "高"),
    ("提高英语发音", "低")
]

# 仅在当天任务列表为空时插入
if not get_today_tasks():
    for task in sample_tasks:
        add_task(task[0], task[1])

# 关闭数据库
conn.close()
