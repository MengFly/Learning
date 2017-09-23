$regfile = "m16def.dat"

$crystal = 8000000

Config portd = Input
Config kbd = portd


Config LcdPin = Pin , Db4 = porta.4 , Db5 = porta.5 , Db6 = PORTA.6 , Db7 = porta.7 , Rs = porta.2 , E = PORTA.3

Dim I as Byte


do
   i = getkbd()
   '如果有按键按下,就显示按下的数字
   if i <> 16 then
      Locate 1 , 1
      waitms 500
      cls
      Lcd I
   end if
Loop

End