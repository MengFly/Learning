$regfile = "m16def.dat"

$crystal = 8000000

Config Portc = Output

Dim A As Byte

Portc = &B11111111 - 1

Wait 1

Do
   For A = 1 To 7
      Rotate Portc , Left                                   '向左移动一个单位
      Wait 1
   Next

   For A = 1 To 7
      Rotate Portc , Right                                  '向右移动一个单位
      Wait 1
   Next
Loop

End