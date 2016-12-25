$regfile = "m16def.dat"
$crystal = 8000000

Dim I as word : I = 0
Dim d(10) as Byte
Dim ADCNumber as word
Dim modx as word

Config porta.3 = Output
Config porta.4 = OUTPUT
Config Portc = OUTPUT

'配置AD转换的端口
Config porta.0 = input
Config porta.1 = input
Config ADC = SINGLE , Prescaler = Auto , Reference = AVCC


'配置AD转换中断以及中断子程序
On ADc adc_isr
Enable interrupts
Enable Adc
'开启AD转换
start adc

restore DuanMa
for i = 1 to 10
   read d(i)
Next
Cls
Do
   idle
Loop

End

adc_isr:
   cls
  ADCNumber = getADC(1)
  'ADCNumber = 1024  测试的数字,测试程序是否正常

  '获取到千位
  i = ADCNumber \ 1000
  incr i
  porta.3 = 1
  portc = d(i)
  porta.3 = 0
  porta.4 = 1
  portc = &B11011111
  porta.4 = 0
  waitms 2

  '获取到百位
  modx = ADCNumber mod 1000
  i = modx \ 100
  incr i
  porta.3 = 1
  portc = d(i)
  porta.3 = 0
  porta.4 = 1
  portc = &B11101111
  porta.4 = 0
  waitms 2

  '获取到十位
  modx = ADCNumber mod 100
  i = modx \ 10
  incr i
  porta.3 = 1
  portc = d(i)
  porta.3 = 0
  porta.4 = 1
  portc = &B11110111
  porta.4 = 0
  waitms 2

  '获取到个位
  i = ADCNumber mod 10
  incr i
  porta.3 = 1
  portc = d(i)
  porta.3 = 0
  porta.4 = 1
  portc = &B11111011
  porta.4 = 0
  waitms 2

Return

DuanMa:
data &B00111111 , &B00000110 , &B01011011 , &B01001111 , &B01100110
data &B01101101 , &B01111101 , &B00000111 , &B01111111 , &B01101111