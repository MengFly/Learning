$regfile = "m16def.dat"  '定义单片机型号'
$crystal = 8000000       '定义晶振频率'

Dim A As Byte            '定义存储左边灯亮的编号'
Dim B As Byte            '定义存储右边灯亮的编号'
Dim Outputlcd As Byte    '定义整体灯亮的编号'
A = &B00000001           '初始化左边灯亮的编号'
B = &B10000000           '初始化右边灯亮的编号'
Dim Tag As Byte : Tag = 0            '标志着灯闪烁的顺序

Config Portc = Output    '配置输出端口'
Do
        '到达中间
   If A = &B00001000 And B = &B00010000 Then
      Tag = 1   '改变灯亮的顺序'
           '到达两侧
   Elseif A = &B00000001 And B = &B10000000 Then
      Tag = 0   '改变灯亮的顺序'
   End If
   Outputlcd = A + B  '根据两边灯的编号获取整体灯亮的编号'
   Portc = &B11111111 - Outputlcd  
   Wait 1

   '计算下一次灯亮的编号'
   If Tag = 0 Then
      A = A * 2    '左边灯向右移动'
      B = B / 2    '右边灯向左移动'
   Else
      A = A / 2    '左边灯向左移动   
      B = B * 2    '右边灯向右移动'
   End If

Loop
End