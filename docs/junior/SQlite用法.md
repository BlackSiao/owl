# 学习SQLite
SQLite是轻量化数据库的最好思路了吧，免安装，功能丰富，而且简单，刚好可以适合新手练手

## 使用命令行
在终端处输入，就可以使用sqlite的命令行编辑功能
```
$ > sqlite3
sqlite> .open test.db          -- 使用点命令打开/创建数据库文件
sqlite> CREATE TABLE apple(    -- 创建表
   ...>   id INTEGER PRIMARY KEY,
   ...>   name TEXT,
   ...>   quantity INTEGER
   ...> );
sqlite> .tables               -- 查看所有表
apple
sqlite> .quit                 -- 退出 
```
## 解析如下：
在 sqlite> 提示符下：

- 输入标准 SQL 语句（不用分号开头）

- 输入 SQLite 点命令（如 .help, .open, .tables 等）

如果看到 ...> 提示符：

- 表示上一条 SQL 语句尚未完整（缺少分号）可以继续输入语句内容
- 完成输入内容后，输入分号 ; 后按回车执行

如果输入错误：
- 按 Ctrl+C 取消当前输入
- 或者输入分号 ; 让系统报错后重新开始

## SQLite的点命令


## SQLite的语法
### 大小写敏感性
SQLite 是**不区分大小写**的，但也有一些命令是大小写敏感的，比如 GLOB 和 glob 在 SQLite 的语句中有不同的含义。

对我来说，关键词写成大写有些难受，本来简单的英语单词，换成大写后，我就不知道写对了没，主要还是习惯问题，我来自非英语国家，平时看到的单词都是小写的。

#### 之所以用大写的原因
历史原因：

    早期 SQL 标准（如 Oracle、IBM DB2）推荐大写关键字，这种风格延续至今。

    旧时代代码编辑器没有语法高亮，大写关键字更容易识别。

可读性：

    大写关键字能让 SQL 语句的结构更清晰，例如：
    sql
    复制

    -- 大写关键字 vs 全小写
    SELECT name, price FROM apple WHERE price > 10;
    select name, price from apple where price > 10;

    对大写版本，人类眼睛能更快定位到关键字（SELECT、FROM、WHERE）。




### 注释
SQL 注释以**两个连续的 "-" 字符**（ASCII 0x2d）开始，并扩展至下一个换行符（ASCII 0x0a）或直到输入结束，以先到者为准。

也可以使用 C 风格的注释，以 "/*" 开始，并扩展至下一个 "*/" 字符对或直到输入结束，以先到者为准。SQLite的注释可以跨越多行。

### SQLite 语句

所有的 SQLite 语句可以以任何关键字开始，如 SELECT、INSERT、UPDATE、DELETE、ALTER、DROP 等，所有的语句以分号 ; 结束。