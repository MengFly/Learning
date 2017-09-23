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


