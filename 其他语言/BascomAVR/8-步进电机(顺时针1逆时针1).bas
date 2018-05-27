$regfile = "m16def.dat"
$crystal = 8000000

Config Portd = output

Dim B(8) As Byte                                            '用于存储步进电机波形的编码的数组
Dim I as Byte                                               '用于存储步进电机端码位置'
Dim X as integer                                            '步进电机端码循环次数'                           

'将数据读入数组
restore BianMa
for i = 1 to 8
   Read B(i)
next

Do
   '顺时针
   gosub ShunShiZhen
   waitms 500
   '逆时针
   gosub NiShiZhen
   waitms 500
Loop


End

'顺时针旋转
ShunShiZhen:
I = 1
For X = 1 to 4096
   portd = B(i)
   incr i
   waitms 1
   if i = 9 then i = 1
Next
Return

'逆时针旋转
NiShiZhen:
I = 8
for x = 1 to 4096
   portd = B(i)
   decr i
   waitms 1
   if i = 0 then i = 8
Next
Return


'步进电机波形的编码
BianMa:
Data &H80 , &HA0 , &H20 , &H60
Data &H40 , &H50 , &H10 , &H90