$regfile = "m16def.dat"
$crystal = 8000000

'配置AD转换的端口
Config porta.0 = input
Config porta.1 = input
Config ADC = SINGLE , Prescaler = Auto , Reference = AVCC

'配置LCD显示屏
Config LcdPin = PIN , Db4 = PORTA.4 , Db5 = PORTA.5 , Db6 = PORTA.6 , Db7 = PORTA.7 , e = PORTA.3 , Rs = PORTA.2
Cursor noblink
Cursor off
Cls

'配置AD转换中断以及中断子程序
On ADc adc_isr
Enable interrupts
Enable Adc
'开启AD转换
start adc

'用来记录AD转换的数字信号
Dim ADCNumber as Word
'用来存储AD转换的模拟信号(电压值)
Dim ADCV as Single
'用来将AD转换的数字信号转换为字符串量
Dim ADCSTR as String * 12
'用来标志获取哪一个AD端口的数据
Dim port as byte : port = 0
'lsb单位伏值,用来计算模拟信号量(电压)
Dim lsb as Single : lsb = 4.8 / 1023

do
   idle
Loop

End

'AD转换的中断子程序
adc_isr:
   ADCNumber = getAdc(port)                                 '从指定的端口获取AD的数字信号
   ADCV = ADCNumber * lsb                                   '根据单位伏特值获取模拟信号量(电压)
   ADCSTR = str(ADCV)                                       '将数字信号量转换为字符串量,便于对结果进行处理
   '根据不同的端口进行不同设置显示
   if port = 0 then
      locate 1 , 1 : Lcd port ; spc(1) ; mid(ADCSTR , 1 , 5) ; "V" ; spc(1) ; "AD:" ; ADCNumber
      port = 1
   else
      locate 2 , 1 : Lcd port ; spc(1) ; mid(ADCSTR , 1 , 5) ; "V" ; spc(1) ; "AD:" ; ADCNumber
      port = 0
   End if
   waitms 5
Return
