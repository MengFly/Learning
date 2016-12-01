'这个函数目的是实现在数码管上面显示数字
'函数参数如下:
'Number  :  要显示的数字
'HasPoint:  要显示的数字带不带有小数点
'Where   :  要显示的数字在那一个位置,可选参数有:w1, w2, w3, w4, w5以及w6
Declare Sub Shownumber(byval Number As Integer , Byval Haspoint As Byte , Byval Where As String)

'这个函数是获取数字对应的二进制编码
'其中这些函数的参数标示:
'Number     :  要显示的数字(在0-9之间,如果不在这之间,就不会显示)
'Haspoint   :  要显示的数字是否带有小数点
Declare Function Getnumbercode(number As Integer , Haspoinnt As Byte) As Integer

'这个函数是获取不同位置的二进制代码
'参数如下:
'where   :  数码管位置.可选参数如下:w1, w2, w3, w4, w5, w6
Declare Function Getwherecode(where As String) As Integer

'这个函数目的是实现在数码管上面显示字符串,目前只支持大写的字母输入,输入时请输入大写的字母
'目前支持的字符串有:A, B, C, D, E. F, G, H, I, J, L, N, O, P, Q, S, T, U, V, X, Y, Z
'函数参数如下:
's       :  要显示的字母
'Where   :  要显示的数字在那一个位置,可选参数有:w1, w2, w3, w4, w5以及w6
Declare Sub Showstring(s As String , Where As String)

'这个函数是获取字母对应的二进制编码
'目前支持的字符串有:A, B, C, D, E. F, G, H, I, J, L, N, O, P, Q, S, T, U, V, X, Y, Z
'其中这些函数的参数标示:
'S     :  要显示的字母(大写)
Declare Function Getstringcode(s As String) As Integer




Sub Shownumber(number As Integer , Haspoint As Byte , Where As String)

   '写入数据并进行锁存
   Porta.3 = 1
   Portc = Getnumbercode(number , Haspoint)
   Porta.3 = 0

   '选择要显示的数码管
   Porta.4 = 1
   Portc = Getwherecode(where)
   Porta.4 = 0

End Sub



Function Getnumbercode(number As Integer , Haspoinnt As Byte) As Integer
   Local Numbercode As Integer
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

   If Haspoinnt = 1 Then
       Numbercode = Numbercode + &B10000000
   End If

   Getnumbercode = Numbercode
End Function


Function Getwherecode(where As String) As Integer
     Local Wherecode As Integer
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

Function Getstringcode(s As String) As Integer
   Local Stringcode As Integer
   Select Case S
      Case "A"
         Stringcode = &B01110111
      Case "B"
         Stringcode = &B01111100
      Case "C"
         Stringcode = &B00111001
      Case "D"
         Stringcode = &B01011110
      Case "E"
         Stringcode = &B01111001
      Case "F"
         Stringcode = &B01110001
      Case "G"
         Stringcode = &B01101111
      Case "H"
         Stringcode = &B01110110
      Case "I"
         Stringcode = &B00000110
      Case "J"
         Stringcode = &B00001111
      Case "L"
         Stringcode = &B00111000
      Case "N"
         Stringcode = &B00110111
      Case "O"
         Stringcode = &B00111111
      Case "P"
         Stringcode = &B01110011
      Case "Q"
         Stringcode = &B01100111
      Case "S"
         Stringcode = &B01101101
      Case "T"
         Stringcode = &B01111000
      Case "U"
         Stringcode = &B00111110
      Case "V"
         Stringcode = &B00111110
      Case "X"
         Stringcode = &B01110110
      Case "Y"
         Stringcode = &B01101110
      Case "Z"
         Stringcode = &B01011011
   End Select
   Getstringcode = Stringcode
End Function

Sub Showstring(s As String , Where As String)
   '写入数据并进行锁存
   Porta.3 = 1
   Portc = Getstringcode(s)
   Porta.3 = 0

   '选择要显示的数码管
   Porta.4 = 1
   Portc = Getwherecode(where)
   Porta.4 = 0
End Sub