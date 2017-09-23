$regfile = "m16def.dat"
$crystal = 8000000

Dim A As Byte
Dim B As Byte
Dim Outputlcd As Byte
A = &B00000001
B = &B10000000
Dim Tag As Byte:Tag = 0                    '标志着灯闪烁的顺序                        

Config Portc = Output
Do
	'到达中间
   If A = &B00001000 And B = &B00010000 Then
      Tag = 1
   	'到达两侧
   Elseif A = &B00000001 And B = &B10000000 Then
      Tag = 0
   End If
   Outputlcd = A + B
   Portc = &B11111111 - Outputlcd
   Wait 1

   If Tag = 0 Then
      A = A * 2
      B = B / 2
   Else
      A = A / 2
      B = B * 2
   End If

Loop
End