$regfile = "m16def.dat"
$crystal = 8000000

Config Portb = &B00001101
Portb = &B11110010

Config Porta = Output
Config Lcd = 16 * 2
Config Lcdpin = Pin , Db4 = Porta.4 , Db5 = Porta.5 , Db6 = Porta.6 , Db7 = Porta.7 , Rs = Porta.2 , E = Porta.3


Dim Ahz(38) As Integer
Dim Atime(38) As Integer
Dim I As Integer : I = 0
Dim Tip As String * 100 : Tip = "AC1 AC2 AC3"

Cls
Do

   If Pinb.1 = 0 Then
     Gosub Music_happy_birthday
   End If

   If Pinb.4 = 0 Then
      Gosub Music_two_tigger
   End If

   If Pinb.5 = 0 Then
      Gosub Music_happy_new_year
   End If

   Cursor Noblink
   Locate 1 , 1 : Lcd "Select Music"
   Locate 2 , 1 : Lcd Tip
   Waitms 500

Loop

End



'播放生日歌
Music_happy_birthday:
  Restore Music_happy_birthday_hz
  For I = 1 To 25
     Read Ahz(i)
  Next I

  Restore Music_happy_birthday_time
  For I = 1 To 25
    Read Atime(i)
  Next

  Cls
  Locate 1 , 1 : Lcd "current muisc"
  Locate 2 , 2 : Lcd "Happy Birthday"
  For I = 1 To 25
     Sound Portb.3 , Atime(i) , Ahz(i)
     Waitms 50
  Next
Return

'播放两只老虎
Music_two_tigger:
   Restore Music_two_tigger_hz
   For I = 1 To 32
      Read Ahz(i) : Ahz(i) = Ahz(i) + 100
   Next

   Restore Music_two_tigger_time
   For I = 1 To 32
      Read Atime(i)
   Next
   Cls
   Locate 1 , 1 : Lcd "current muisc"
   Locate 2 , 4 : Lcd "Two Tigger"
   For I = 1 To 32
      Sound Portb.3 , Atime(i) , Ahz(i)
      'Print Atime(i) ; " --- " ; Ahz(i)
      Waitms 50
   Next

Return

'播放新年好
Music_happy_new_year:
   Restore Music_happy_new_year_hz
   For I = 1 To 32
      Read Ahz(i) : Ahz(i) = Ahz(i) + 100
   Next

   Restore Music_happy_new_year_time
   For I = 1 To 32
      Read Atime(i) : Atime(i) = Atime(i) * 1000
   Next
   Cls
   Locate 1 , 1 : Lcd "current muisc"
   Locate 2 , 2 : Lcd "Happy New Year"
   For I = 1 To 32
      Sound Portb.3 , Atime(i) , Ahz(i)
      'Print Atime(i) ; " --- " ; Ahz(i)
      Waitms 50
   Next
   Cls
Return

'生日歌的赫兹
Music_happy_birthday_hz:
Data 212% , 212% , 190% , 212% , 159% , 169% , 212% , 212%
Data 190% , 212% , 142% , 159% , 212% , 212% , 106% , 126%
Data 159% , 169% , 190% , 119% , 119% , 126% , 159% , 142%
Data 159%
'生日歌的时间
Music_happy_birthday_time:
Data 900% , 300% , 1200% , 1200% , 1200% , 2400% , 900% , 400%
Data 1200% , 1200% , 1200% , 2400% , 900% , 600% , 1200% , 1200%
Data 1200% , 1600% , 1600% , 1000% , 1000% , 1400% , 1400% , 1400%
Data 3000%

'两只老虎赫兹
Music_two_tigger_hz:
Data 13% , 15% , 17% , 13%
Data 13% , 15% , 17% , 13%
Data 17% , 18% , 20%
Data 17% , 18% , 20%
Data 20% , 22% , 20% , 18% , 17% , 13%
Data 20% , 22% , 20% , 18% , 17% , 13%
Data 15% , 8% , 13%
Data 15% , 8% , 13%

'两只老虎时间
Music_two_tigger_time:
Data 2000% , 2000% , 2000% , 2500%
Data 2000% , 2000% , 2000% , 2500%
Data 2000% , 2000% , 2500%
Data 2000% , 2000% , 2500%
Data 1000% , 1000% , 1000% , 1000% , 2000% , 2000%
Data 1000% , 1000% , 1000% , 1000% , 2000% , 2000%
Data 2500% , 2500% , 2500%
Data 2600% , 2800% , 3000%


Music_happy_new_year_hz:
Data 13 % , 13 % , 13 % , 8%
Data 17 % , 17 % , 17 % , 13%
Data 13 % , 17 % , 20 % , 20%
Data 18 % , 17 % , 15 % , 0%
Data 15 % , 17 % , 18 % , 18%
Data 17 % , 15 % , 17 % , 13%
Data 13 % , 17 % , 15 % , 8%
Data 12 % , 15 % , 13 % , 0%

Music_happy_new_year_time:
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%
Data 1% , 1% , 2% , 2%