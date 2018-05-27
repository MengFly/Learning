$regfile = "m16def.dat"	 '定义单片机型号'		
$crystal = 8000000		 '定义晶振频率'	

'配置端口'
Config portd = Input	
Config kbd = portd

'配置液晶显示屏'
Config LcdPin = Pin , Db4 = porta.4 , Db5 = porta.5 , Db6 = PORTA.6 , Db7 = porta.7 , Rs = porta.2 , E = PORTA.3

'定义存储按键代码的变量'
Dim I as Byte

do
   i = getkbd()		'获取按键代码'
   '如果有按键按下,就显示按下的数字
   if i <> 16 then
      Locate 1 , 1
      waitms 500
      cls
      Lcd i 	'显示'
   end if
Loop

End