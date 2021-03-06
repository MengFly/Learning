# 程序效果

## [1-LED灯显示](1-LED灯显示.bas)
这个程序在单片机上面的效果是八个LED灯从两端向中间依次显示,到达中间后再向两侧依次显示

## [2-跑马灯](2-跑马灯.bas)
LED跑马灯效果

## [3-showLove.bas](3-showLove.bas)

这个程序是在数码管上面依次显示I Love You 这三个单词

## [4-NumberAndCharCode.bas](4-NumberAndCharCode.bas)
这个程序里面写了几个函数和子过程,里面包含了所有能在数码管上面显示的**数字**和**字符**的二进制代码

## [5-查询按键输入--抢答器](5-查询按键输入--抢答器.bas)
这是一个抢答器的程序
程序开始会在LCD灯上面提示抢答
抢答是如果有一个按键先按下去就不允许其他的按键再进行输入了
当所有按键都抬起的时候,程序会在LCD上面显示程序恢复的时间(20S)
20S后程序恢复到初始状态,恢复的这二十秒时间里面不接受任何按键
之后就可以再一次进行抢答了

## [6-蜂鸣器](6-蜂鸣器.bas)
使用蜂鸣器去播放音乐,这个程序里面有三个音乐,分别是**生日快乐**,**两只老虎**,**新年好**
程序开始的时候会在LCD显示屏上面显示字符串让使用者选择歌曲
当点击按键AC1的时候播放生日快乐
当点击按键AC4的时候播放两只老虎
当点击按键AC5的时候播放新年好

## [7-蜂鸣器(简单响起)](7-蜂鸣器\(简单响起\).bas)
让蜂鸣器响起来的程序

## [8-步进电机(顺时针1逆时针1)](8-步进电机\(顺时针1逆时针1\).bas)
步进电机顺时针转一圈逆时针转一圈

##[9-步进电机(可调速以及方向)](9-步进电机(可调速以及方向).bas)
这个例子程序里面可以调控步进电机的速度和旋转方向,以及步进电机是否开始转动
A1 : 步进电机转速最快的档位
A4 : 步进电机转速中速的档位
A5 : 步进电机转速最慢的档位
A6 : 控制步进电机的转动方向
A7 : 控制步进电机是否转动

## [10-4x4小键盘测试](10-4x4小键盘测试.bas)
按键在Lcd显示屏上面显示数字

## [11-中断测试(数码管)](11-中断测试\(数码管\).bas)
这个程序用于测试中断,正常情况下,数码管上面的光标沿着逆时针旋转,当点击Int0按钮的时候数码管就沿着顺时针旋转,当点击Int1按钮的时候数码管就沿着逆时针旋转

## [12-定时计时器测试程序](12-定时器的使用.bas)
这个程序是用来测试定时计数器的
效果如下:
程序运行的时候步进电机会顺时针旋转3秒,逆时针旋转3秒,来回循环
如果按下AC1键的话,会关闭定时器,这时候电机将不会来回旋转

## [13-AD转换(烟雾报警器).bas](13-AD转换\(烟雾报警器\).bas)
这个程序是烟雾报警器的程序,因为用到了AD转换,所以实际中单片机中的AD转换的数字会在数码管上面显示出来
当这个数值大于300的时候,讯响器就会报警,从而实现烟雾报警的作用

## [14-AD转换(AD0AndAD1).bas](14-AD转换\(AD0AndAD1\).bas)
这个程序是显示AD转换后的数字信号以及模拟信号(**电压量**),改变AD0和AD1的阻值,在LCD上面就会显示相应的电压值以及数字信号

## [15-AD转换(数码管).bas](15-AD转换\(数码管\).bas)

这个程序是AD转换的数字显示在数码管上面的程序

## [16-除法测试.bas](16-除法测试.bas)
之前在做AD转换的时候,发现对数字进行整除的时候数据一直不对,最后把里面的数据类型全部都换成**word**就可以了,今天**2016-12-25**其他同学也遇到了这个问题,我就做了一个测试.测试内容是:
 我用两个整型**(Integer)**的变量去做整除,结果用一个**Byte**类型去接受.看看如果Integer的类型如果超过了byte的范围会出现什么情况
 测试如下:
  + z(**byte**) = y(**Integer:260**)\x(**Integer:257**)  *结果z=4*
  + z(**byte**) = y(**Integer:200**)\x(**Integer:260**)  *结果z=50*
  + z(**byte**) = y(**Integer:260**)\x(**Integer:5**)  *结果z=0*
  + z(**byte**) = y(**Integer:200**)\x(**Integer:5**)  *结果z=40*
    结果和我预料的一样
    例如第一个结果按照正常的结果应该是1,结果却是4那么程序做了一下动作
   1. 将y转换为byte类型数据,这时候y = 260 - 256 = 4
   2. 将x转换为byte类型数据,这时候x = 257 - 256 = 1
   3. 将y对x进行整除,得到结果(4 \ 1 = 4),这时候就会得到我们看到的结果了
      其余下面的结果就和第一种情况相似,也是用同一种方法来分析,就可以发现只是把后面的Integer变量转换成了Byte类型而已,对一那些被除数大于256的,结果肯定会和我们想要的结果不一致.
