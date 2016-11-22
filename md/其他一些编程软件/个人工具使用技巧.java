# 查看占有端口号的应用是那个应用
# 其中5037就是要查看的端口号
# 查询的结果就是
# TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       6096
# TCP    127.0.0.1:5037         127.0.0.1:49954        ESTABLISHED     6096
# TCP    127.0.0.1:5037         127.0.0.1:49967        ESTABLISHED     6096
# TCP    127.0.0.1:5037         127.0.0.1:49969        ESTABLISHED     6096
# 可以看到是后面的PID 为6096的进程占用了端口5037，之后主要在资源管理器里面找到PID为6096的应用，停掉就可以了
netstat -aon|findstr "5037"


# 获取正在运行的service
get-service | where-object {$_.Status -eq "Running"}
# 获取停止的Service
get-service | where-object {$_.Status -eq "Stopped"}
# 获取Service可访问的变量和方法
get-service | get-member
# 根据所选的类型进行排序
get-service s* | sort-object status [-descending](反向排序)

115.28.188.113:8080

#设置WindowPower支持其他模块的ps1文件，可以设置策略模式
set-ExecutionPolicy RemoteSigned

#使Powershell支持高亮
(new-object Net.WebClient).DownloadString("http://psget.net/GetPsGet.ps1") | iex
Set-ExecutionPolicy RemoteSigned
Install-Module PSReadLine


Sublime==========================================================
使用插件Advance New File；
使用快捷键Ctrl+Alt+N，输入文件夹/文件名即可创建文件
使用Alt + . 可以补全Html里面的标签
使用Emmet插件可以快速编辑Html文件
安装Emmet插件后使用快捷键 Ctrl+ E 可以快速编辑Html文件
例如 ： ul>.item$*10可以生成一个ul下面有10个li的标签

