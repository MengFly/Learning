# Android软件测试
[TOC]
## App压力测试
+ 为什么要开展压力测试
提高产品的稳定性
提高产品的留存率

+ 什么时候进行压力测试
首轮测试通过后
下班后的夜间进行

## 第二部分--理论
手工测试场景--模拟事件流
只要模拟出来事件流,我们就可以实现自动化测试

### Monkey
是发送伪随机事件的工具
存在于手机里面

### MonkeyScript
是一组可以被Monkey识别的命令集合
和一完成重复的操作
但是他不支持截屏的操作

### MonkeyRunner
通过API定义的特定命令和事件控制设备
+ MonkeyRunnner
用来连接设备或模拟器
+ MonkeyDevice
用来安装,卸载应用,发送模拟事件
+ MonkeyImage
完成图像保存,以及对比操作
+ 用途
多设备测试
功能测试
回归测试

### 异常结果分析:
Crash
ANR(Application Not Respinding)

### 需要准备的工具:
+ Android SDK
+ Python

#### 下载Android SDK
官方网站或者(www.android-studio.org)

#### 下载Python
www.python.org/downloads

## 具体测试
###  查看连接的设备
	adb devices

### 安装APK
	adb install package.apk

### 压力指令:
	adb shell monkey 1000		(随机进行1000次操作)

### 获取应用包名
	[Linux] adb logcat | grep START
	[WINDOWS] adb logcat | findstr START
或者输入命令
	adb shell	进入adb命令行
	之后输入
	logcat | grep START		查找包名

### 给指定的应用打压力
	adb shell monkey -p package 1000	给指定的包执行1000次操作

### monkey高级参数

#### throttle参数
		指定事件之间的间隔
		adb shell monkey --throttle <milliseconds>(毫秒数)

adb shell monkey -p com.android.calculator2 --throttle 1000 100
每个事件之间间隔1秒

#### seed 参数
	怎么复现出错流程,利用seed参数可以执行相同操作序列
	相同的seed值执行的操作是一样的,可以利用seed值对错误进行复现
	adb shell monkey -s<seed><event-count>
adb shell monkey -v -p com.android.calculator2 -s 100 -- throttle 10 50
-v 会把执行的所有操作进行列出来

### 触摸事件
	设定触摸事件的百分比
	adb shell monkey  --pct-touch <percent>	--点击事件
adb shell monkey -v -p com.android.calculator2 --pct-touch 100 50	设定点击事件百分比为百分之百
不指定的话,各个事件的百分比会随机分布


### 其他事件
#### 	动作事件
		--pct-motion <percent>
#### 	轨迹球事件
		--pct-trackball <percent>
#### 	基本导航事件
		输入设备的上下左右
		--pct-nav <percent>
#### 	主要导航事件
		兼容中间键,返回键,菜单按键
		--pct-majornav <percent>
#### 	系统导航事件
		HOME,BACK,拨号键以及音量键
		--pct-syskeys <percent>
#### 	启动Activity事件
		设定启动activity的事件百分比
		--pct-appswitch <percent>
#### 	不常用事件
		--pct-anyevent <percent>

### 崩溃事件
	忽略崩溃和异常
	adb shell monkey --ignore-crashes<event-count>
	忽略event-count次的异常

### 超时事件
	忽略超时事件
	adb shell monkey --ignore-timeouts <event-count>
	忽略event-count次的异常

#### Crash结果析取
	adb shell monkey -p com.example.econonew --throttle 100 --ignore-crashes --ignore-timeouts 1000

### 保存测试信息到计算机
如果我们想要计算机进行自动化测试,再来查看测试信息的话我们可以在后面添加这么一行
... | out-file -filepath filename
来对测试的数据进行保存

### MonkeyScript 常用命令的介绍
	实现重复操作100次(完成一些固定的操作)

#### 执行Monkey脚本命令
	adb shell monkey -f <scriptfile> <event-count>

#### 	脚本命令
##### DispatchTrackball命令
		轨迹球事件
**DispatchTrackball**(long downtime, long eventtile, int action, float x, float y, float pressure, float size, int metastate, float xprecision, float yprecision, int device, int edgeflags)
可以帮助我们完成点击事件
 - downtime:键最初被按下的时间
 - eventide:事件发生的时间
 - action: 具体的操作事件
 - x, y: 坐标点
 - pressure:范围 0-1
 - size:0-1
 - metastate:当前按下meta键的标示
 - x,yprecision:按下的x和y坐标的精确值
 - device:事件的来源
 - edgeflags:超出屏幕的范围
 - 这里面只用关注x, y, action
 - 其他的参数我们设置初始值就可以了
 - action 0(按下), 1(弹起)


##### DispatchPointer
点击事件
**DispathPointer**(long downtime, long eventide, int action, float x, float y, float pressure, float size, int metastate, float xprecision, float yprecision, int device, int edgeflags)

 - DispatchString
		输入字符串事件
			DispatchString(String text)

 - LaunchActivity
		启动应用
		LaunchActivity(package, Activity)

 - UserWait
		等待时间
		UserWait(time)

 - DispatchPress
		按下键值
		DispatchPress(int keycode) #keycode 66 回车键
通过android sdk下面的tools文件下面的工具:uiautomatorviewer可以查看屏幕具体位置

#### 实例:
```
//通用设置
typ=user
count=10
speed=1.0
start data >>

LaunchActivity(com.example.econonew, com.example.econonew.view.activity.main.SplashActivity) //启动主Activity
UserWait(2000) //等待2秒
DispatchPointer(10, 10, 0, 100, 100, 1, 1, -1, 1, 1, 0, 0)//在100, 100的位置按下
DispatchPointer(10, 10, 1, 100, 100, 1, 1, -1, 1, 1, 0, 0)//在100, 100的位置抬起
DispatchString(test)//输入test字符串
UserWait(1000)//等待1秒钟
DispatchPress(66)//按下回车键
UserWait(1000)//等待1秒钟
DispatchPointer(10, 10, 0, 400, 100, 1, 1, -1, 1, 1, 0, 0)//在400, 100的位置按下
DispatchPointer(10, 10, 1, 400, 100, 1, 1, -1, 1, 1, 0, 0)//在400, 100的位置抬起
UserWait(6000)//等待6秒钟
DispatchPointer(10, 10, 0, 300, 100, 1, 1, -1, 1, 1, 0, 0) //在300， 100 的位置按下
DispatchPointer(10, 10, 1, 300, 100, 1, 1, -1, 1, 1, 0, 0) //在300， 100 的位置抬起
UserWait(3000)//等待3秒钟
```
之后将脚本文件push到手机里面
使用命令：

	adb push filename.script path
	例如：
		adb push mook.script /data/local/tmp
之后进入手机的相关目录
之后就可以执行脚本文件了
但是要想在外部启动相应的App，在这个App的Mainifast文件里面必须设置Activity的exported=true属性
这样App才可以被外部启动

### MonkeyRunner
	MonkeyRunner可以实现截屏
保存文件,文件名自定
运行:
	monkeyrunner monkeyrunnerfilePath
就可以执行了

#### MonkeyRunner API --alert
警告框

    void alert(String message, String title, String okTitle)
例如:

    from com.android.monkeyrunner import MonkeyRunner
	MonkeyRunner.alert("Hello I'm Message", "This is Title", "I'm Button")




#### MonkeyRunner API -waitForConnection
	等待设备连接,有多个device id , 需要指明具体那个设备
	WaitForConnection(float timeout, String deviceid)


#### MonkeyDevice API -drag
拖动
	drag(tuple start, tuple end, float duration, integer steps)
	start:起点位置
	end:终点位置
	duration:手势持续的时间
	steps:插值点的步数, 默认10

#### MonkeyDevice API -press
按键
	press(String keycode, dictionary type)
	type:Down, UP, DOWN_AND_UP

#### MonkeyDevice API -startActivity
启动应用
	startActivity(package+"/"+activity)

#### MonkeyDevice API -touch
点击
	touch(integer x, integer y, integer type)
	type:DOWN, UP, DOWN_AND_UP

#### MonkeyDevice APU -type
输入
	type(message)

#### MonkeyDevice API -tackSnapshot
截屏
	MonkeyImage takeSnapshot()

#### MonkeyImage API -sameAs
图相对比
	boolean sameAs(MonkeyImage other, float percent)
	percent:对比的百分比

#### MonkeyImage API -writeFile
保存图像文件
	void writeToFile(String path, String format)
	format:图像的类型(jpg,png...)

#### MonkeyRunner实践

+ 要支持中文的话,请在程序的第一行加上:
	# coding=utf-8

```python
#coding=utf-8
# 导入相关MonkeyRunner API
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# 连接设备
device = MonkeyRunner.waitForConnection(3, "192.168.173.101:5555")

#启动APP
device.startActivity("com.example.econonew/com.example.econonew.view.activity.main.SplashActivity")

MonkeyRunner.sleep(2)

#点击100, 100 的位置
device.touch(100, 100, "DOWN_AND_UP")

MonkeyRunner.sleep(1)

# 输入单词
device.type('test')

MonkeyRunner.sleep(1)

# 点击回车键
device.press('KEYCODE_ENTER', 'DOWN_AND_UP')

MonkeyRunner.sleep(1)

# 点击400, 100 的位置
device.touch(400, 100, "DOWM_AND_UP")

MonkeyRunner.sleep(6)

# 截图
image = device.takeSnapshot()
image.writeToFile('../test.png', 'png')
```

要想要MonkeyRunner进行多次操作的话,就得需要我们使用
python脚本进行多次操作了













