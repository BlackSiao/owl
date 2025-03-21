import sqlite3

# 连接数据库
with sqlite3.connect("Daily.db") as daily_conn:
    cursor = daily_conn.cursor()

    # 查询 tasks 表的所有数据
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()  # 获取所有查询结果

    # 打印表数据
    for task in tasks:
        print(task)