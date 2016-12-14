$regfile = "m16def.dat"
$crystal = 8000000

'配置PortD,控制步进电机
Config Portd = output

'配置PortB用于按键查询
Config PortB = input
PortB = &B11110010

'配置Lcd显示
Config LcdPin = PIN , Db4 = PORTA.4 , Db5 = PORTA.5 , Db6 = Porta.6 , Db7 = Porta.7 , Rs = Porta.2 , E = PORTA.3

Config Timer0 = Timer , Prescale = 8
On ovf0 timer0_isr
Enable ovf0
Enable interrupts
Load timer0 , 200
Start Timer0


'Bit 类型变量,用于标志步进电机是顺时针旋转,还是逆时针旋转
Dim b as Bit : b = 0
'用于存储步进电机波形的编码的数组
Dim Da(8) as Byte
Dim i As Byte
'标志计数器执行的次数，Load Timer0,200，分频数为8，主频为8M时，执行5000次为1S
Dim timer_counts as Integer : timer_counts = 0
'标志计时器是否开启
Dim is_start_timer as bit : is_start_timer = 1

'将数据读入数组
restore DaiMa
for i = 1 to 8
   Read Da(i)
next
Cls
Do
   if b = 0 then
      incr i
      if i = 9 then i = 1
   else
      decr i
      if i = 0 then i = 8
   end if
   waitms 1
   portd = Da(i)

   if pinb.1 = 0 then
      Cls
      if is_start_timer = 1 then
         Locate 1 , 1 : Lcd "Timer Stop!!!"
         Stop Timer0
         is_start_timer = 0
      else
         Locate 1 , 1 : Lcd "Timer Start!!!"
         Start timer0
         is_start_timer = 1
      End if
      Waitms 500
   End if
Loop


End


DaiMa:
Data &H80 , &HA0 , &H20 , &H60
Data &H40 , &H50 , &H10 , &H90

Timer0_isr:
   Load Timer0 , 200
   '执行5000次的时候正好是1S，执行三秒
   if timer_counts = 15000 then
      Cls
      Locate 1 , 1 : Lcd "Timer Start!!!"

      '重置计数
      timer_counts = 0
      if b = 0 then
         Locate 2 , 1 : Lcd "Shun Shi Zhen"
         b = 1
      else
         Locate 2 , 1 : Lcd "Ni Shi Zhen"
         b = 0
      End if
   else
      incr timer_counts
   End if
Return
