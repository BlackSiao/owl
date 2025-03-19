## tar命令

tar命令是Linux和Unix系统中用于**归档文件和目录**的其命令行工具。

首先要声明的就是归档文件并不是指压缩文件，可以理解tar命令只是把文件给打包了，而压缩是其他压缩工具的事情。

语法：
```
tar [options] -f archive.tar [files...]
# archive.tar：指定归档文件的名称
# [files...]: 指定要打包的文件和目录
```