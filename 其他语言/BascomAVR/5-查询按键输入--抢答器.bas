$regfile = "m16def.dat"
$crystal = 8000000

'重新开始游戏'
Declare Sub Restart()
'液晶屏显示胜利者'
'params:user 胜利者'
Declare Sub Showwiner(user As String * 4)
'显示等待时间'
Declare Sub Waittime()

Config Portb = &B00001101
Portb = &B11110010                                          'B端口高四位和第一位上拉电阻有效

'配置液晶显示屏'
Config Porta = Output
Config Lcd = 16 * 2
Config Lcdpin = Pin , Db4 = Porta.4 , Db5 = Porta.5 , Db6 = Porta.6 , Db7 = Porta.7 , Rs = Porta.2 , E = Porta.3

'用于存储胜利者的标识'
Dim Winerkey As String * 4
'用于存储按键输入标识'
Dim Incode As Byte

'变量标志游戏有没有开始,0为没有开始,1标示游戏已经开始
Dim Isstartgame As Bit

'游戏开始'
Call Restart()
Do
  '获取输入'
   Incode = Pinb

   '如果当前没有确定赢家,就进入if语句去确定赢家
   If Winerkey = "none" Then
       If Incode.7 = 0 Then
          Winerkey = "AC7"
         Elseif Incode.6 = 0 Then
             Winerkey = "AC6"
         Elseif Incode.5 = 0 Then
             Winerkey = "AC5"
         Elseif Incode.4 = 0 Then
             Winerkey = "AC4"
         Elseif Incode.1 = 0 Then
            Winerkey = "AC1"
       End If

     '如果当前存在赢家,如果现在所有按键都没有被按下,说明这一轮游戏已经结束,重置赢家,准备下一局游戏
   Else
      If Incode.7 <> 0 And Incode.6 <> 0 And Incode.5 <> 0 And Incode.4 <> 0 And Incode.1 <> 0 Then
         Call Waittime()
         Call Restart()
      End If
   End If

   '如果当前存在赢家,那么就显示这个赢家
   If Winerkey <> "none" Then
         Call Showwiner(winerkey)
   End If
Loop
End


Sub Restart()
  '重置胜利者标识'
   Winerkey = "none"
   Isstartgame = 0
   Cls
   '游戏开始时的提示文字
   Locate 1 , 1 : Lcd "Plase Enter Key"
   Locate 2 , 2 : Lcd "To Start Game"
End Sub

Sub Showwiner(user As String * 4)
   '如果游戏是第一次启动,那么就进行清屏,放置刚开始的提示文字对之后要显示的文字产生影响
   If Isstartgame = 0 Then
      Cls
      Isstartgame = 1
   End If
   '显示胜利者'
   Locate 1 , 1 : Lcd "The Winer is :"
   Locate 2 , 2 : Lcd "User" ; Spc(1) ; ":" ; Spc(1) ; User
End Sub

'所有人都抬起的时候过去20秒钟的时候才可以进行抢答
Sub Waittime()
   Local I As Byte
   For I = 20 To 1 Step -1
       Wait 1
       '格式化数字，大于10不变，小于10前面加0'
       If I > 9 Then
         Locate 2 , 15 : Lcd I
         Else
         Locate 2 , 15 : Lcd "0" ; I
       End If
   Next
End Sub
