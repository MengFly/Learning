$regfile = "m16def.dat"
$crystal = 8000000
Config Portc = output
Config porta.3 = output
Config Porta.4 = output

porta.4 = 1
portc = &HFF
Porta.4 = 0
porta.3 = 1

Config Int0 = Falling
Config Int1 = FALLING

On Int0 int0_isr
on Int1 int1_isr
Enable Interrupts                                           '开启全局中断
Enable Int0                                                 '开启Int中断
Enable Int1                                                 '开启Int1中断

Dim A(7) as Byte
Dim I as Byte

Restore Daima
   For i = 1 to 6
      Read A(i)
   Next I

'这个变量标志这数码管是顺时针旋转还是逆时针旋转,1为顺时针,0为逆时针
Dim run as bit : run = 0

I = 1

Do
   if run = 1 then
      gosub Shun
   else
      gosub Ni
   end if
   Portc = A(i)
   WAITMS 500
Loop
End


'数码管显示的代码(顺时针旋转)
DaiMa:
Data &B00100000 , &B00010000 , &B00001000 , &B00000100 , &B00000010 , &B00000001

'顺时针旋转的子过程
Shun:
   incr i
   if i > 6 then i = 1
return

'逆时针旋转的子过程
Ni:
   decr i
   if i < 1 then i = 6

return

'Int0的程序
Int0_isr:
   run = 0
return

'Int1的程序
Int1_isr:
   run = 1
return
