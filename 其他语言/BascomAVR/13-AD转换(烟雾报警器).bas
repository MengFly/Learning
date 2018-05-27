'获取到数字对应的二进制端码
Declare Function GetNumberCode(number as word) as byte
'在数码管指定位置显示数字
Declare Sub Shownumber(byval Number As word , Byval Where As String)
'获取到在数码管那里显示的端码
Declare Function Getwherecode(where As String) As byte

$regfile = "m16def.dat"
$crystal = 8000000

'配置AD转换,使用的是AVCC,内部参考电压是5V
Config Porta.7 = input
Config ADC = SINGLE , Prescaler = AUTO , Reference = AVCC

'配置数码管,用于显示转换的数字
Config porta.4 = OUTPUT
Config porta.3 = OUTPUT
Config Portc = OUTPUT

'用于讯响器,进行烟雾报警
Config Portb.3 = OUTPUT

'用于接收AD转换后的数字
Dim ADNumber as word
'i和i2用于对接受到的AD数字进行运算，从而得到他的个位十位百位千位从而在数码管上面进行显示
dim i as word
dim i2 as word
'在数码管的哪一个位置显示
dim where as String * 2
Do
  ADNumber = getadc(7)
  gosub showADNumber

  '根据不同的指标进行不同的报警声音
  if ADNumber > 300 then
      sound portb.3 , 10 , 1276
  elseif ADNumber > 500 then
      sound portb.3 , 10 , 956
  elseif ADNumber > 700 then
      sound portb.3 , 10 , 568
  elseif ADNumber > 900 then
      sound portb.3 , 10 , 426
  end if

Loop

End

'显示AD转换后的数字的子过程
showADNumber:
   '获取到千位并进行显示
   i = ADNumber \ 1000
   where = "w6"
   call showNumber(i , where)
   waitms 5

   '获取到百位并进行显示
   where = "w5"
   i2 = ADNumber mod 1000
   i = i2 \ 100
   call showNumber(i , where)
   waitms 5

   '获取到十位进行显示
   where = "w4"
   i2 = ADNumber mod 100
   i = i2 \ 10
   call showNumber(i , where)
   waitms 5

   '获取到个位进行显示
   where = "w3"
   i = ADNumber mod 10
   call showNumber(i , where)
   waitms 5
Return

'获取到数字对应的二进制端码
Function Getnumbercode(number As word) As byte
   Local Numbercode As byte : NumberCode = 1
   Select Case Number
      Case 0
         Numbercode = &B00111111
      Case 1
         Numbercode = &B00000110
      Case 2
         Numbercode = &B01011011
      Case 3
         Numbercode = &B01001111
      Case 4
         Numbercode = &B01100110
      Case 5
         Numbercode = &B01101101
      Case 6
         Numbercode = &B01111101
      Case 7
         Numbercode = &B00000111
      Case 8
         Numbercode = &B01111111
      Case 9
         Numbercode = &B01101111

   End Select

   Getnumbercode = Numbercode
End Function

'在数码管指定位置显示数字
Sub Shownumber(number As word , Where As String)
   '写入数据并进行锁存
   Porta.3 = 1
   Portc = Getnumbercode(number)
   Porta.3 = 0

   '选择要显示的数码管
   Porta.4 = 1
   Portc = Getwherecode(where)
   Porta.4 = 0

End Sub

'获取到在数码管那里显示的端码
Function Getwherecode(where As String) As byte
     Local Wherecode As byte
     Select Case Where
      Case "w1"
         Wherecode = &B11111110
      Case "w2"
         Wherecode = &B11111101
      Case "w3"
         Wherecode = &B11111011
      Case "w4"
         Wherecode = &B11110111
      Case "w5"
         Wherecode = &B11101111
      Case "w6"
         Wherecode = &B11011111
   End Select
   Getwherecode = Wherecode
End Function