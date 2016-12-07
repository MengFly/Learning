'运行步进电机
'参数说明
'Speed : 速度,传入等待时间
'direction : 方向, 默认为顺时针方向
Declare Sub RunMotor()

Declare Sub CheckSpeedAndDirectionAndStart()
$regfile = "m16def.dat"
$crystal = 8000000

Config Portb = Input
portb = &B11110001
Config Portd = output

Dim B(8) As Byte                                            '用于存储步进电机波形的编码的数组
Dim I as Byte
Dim Speed as Byte : speed = 1                               '标志速度
Dim direction as String * 4 : direction = "Shun"            '标志旋转方向
Dim isStart as Bit : isStart = 0
'将数据读入数组
restore BianMa
for i = 1 to 8
   Read B(i)
next
Do
   call CheckSpeedAndDirectionAndStart()
   if isStart = 0 then call RunMotor()
Loop
End

Sub RunMotor()
   If direction = "Shun" then
      i = i + 1
      if i = 9 then i = 1
   else
      i = i - 1
      if i = 0 then i = 8
   end if
   portd = B(i)
   waitms speed
End sub

Sub CheckSpeedAndDirectionAndStart()
   if Pinb.1 = 0 then
      Speed = 1
   elseif Pinb.4 = 0 then
      Speed = 2
   elseif pinb.5 = 0 then
      Speed = 4
   end if

   if pinb.6 = 0 then
      if direction = "Shun" then
         Direction = "Ni"
      else
         direction = "Shun"
      end if
      waitms 500
   end if

   if Pinb.7 = 0 then
      if isStart = 0 then
         isStart = 1
      else
         isStart = 0
      end if
      waitms 500
   end if

end Sub

'步进电机波形的编码
BianMa:
Data &H80 , &HA0 , &H20 , &H60
Data &H40 , &H50 , &H10 , &H90