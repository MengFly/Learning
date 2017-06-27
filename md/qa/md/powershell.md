[TOC]

## 修改Powershell执行策略
> 默认设置为最安全的策略“Restricted”。该设置允许运行单个命令，但不允许运行脚本。

+ Set-ExecutionPolicy RemoteSigned //开启允许加载未签名的脚本运行
+ Set-ExecutionPolicy Restricted //不允许加载未签名的脚本运行
+ Get-ExecutionPolicy //查看当前的执行策略

## 在桌面上面创建快捷方式
```powershell
# filePath 为文件的绝对路径,不可写错了,否则将会在桌面创建一个无效的路径
# linkName 为要在桌面创建的快捷方式的名称
function link($filePath, $linkName) {

	# 我们要使用到COM组件，在Powershell中获取COM组件
	$shell = New-Object -ComObject WScript.shell

	#获取桌面位置
	$desktop = [System.Environment]::GetFolderPath('Desktop')

	# 定义快捷方式对象,并设置他的属性
	$shortcut = $shell.CreateShortcut("$desktop\$linkName.lnk")
	$shortcut.TargetPath = "$filePath"

	# 保存设置
	$shortcut.Save()

}
```
## 批量修改文件名称
``` powershell
get-childitem *.txt | rename-item -newname {$_.name -replace '.txt' , '.html'}

get-childitem (获取到我们想要修改的文件)
rename-item (对获取到的文件进行修改名称)
{$_.name -replace '.txt' , '.html'} (指定新文件的名称)


```