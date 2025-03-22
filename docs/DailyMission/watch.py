import sqlite3
from datetime import datetime

# 查看今天的数据库里面有些什么内容了

# 获取今天的表名
today = datetime.today().strftime('%Y_%m_%d')

# 连接数据库
with sqlite3.connect("Daily.db") as daily_conn:
    cursor = daily_conn.cursor()

    # 查询今天的任务表
    cursor.execute(f'SELECT * FROM "{today}"')  # 确保表名用双引号包裹
    tasks = cursor.fetchall()  # 获取所有查询结果

    # 打印表数据
    if tasks:
        print(f"=== {today} 的任务列表 ===")
        for task in tasks:
            task_id, task_name, priority, completed = task
            status = "✔️ 已完成" if completed else "❌ 未完成"
            print(f"[{task_id}] {task_name} - 优先级: {priority} - 状态: {status}")
    else:
        print(f"=== {today} 没有任务 ===")
