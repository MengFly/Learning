'���в������
'����˵��
'Speed : �ٶ�,����ȴ�ʱ��
'direction : ����, Ĭ��Ϊ˳ʱ�뷽��
Declare Sub RunMotor()

Declare Sub CheckSpeedAndDirectionAndStart()
$regfile = "m16def.dat"
$crystal = 8000000

Config Portb = Input
portb = &B11110001
Config Portd = output

Dim B(8) As Byte                                            '���ڴ洢����������εı��������
Dim I as Byte
Dim Speed as Byte : speed = 1                               '��־�ٶ�
Dim direction as String * 4 : direction = "Shun"            '��־��ת����
Dim isStart as Bit : isStart = 0
'�����ݶ�������
restore BianMa
for i = 1 to 8
   Read B(i)
next
Do
   call CheckSpeedAndDirectionAndStart()
   if isStart = 0 then call RunMotor()
Loop
End

Sub RunMotor()
   If direction = "Shun" then
      i = i + 1
      if i = 9 then i = 1
   else
      i = i - 1
      if i = 0 then i = 8
   end if
   portd = B(i)
   waitms speed
End sub

Sub CheckSpeedAndDirectionAndStart()
   if Pinb.1 = 0 then
      Speed = 1
   elseif Pinb.4 = 0 then
      Speed = 2
   elseif pinb.5 = 0 then
      Speed = 4
   end if

   if pinb.6 = 0 then
      if direction = "Shun" then
         Direction = "Ni"
      else
         direction = "Shun"
      end if
      waitms 500
   end if

   if Pinb.7 = 0 then
      if isStart = 0 then
         isStart = 1
      else
         isStart = 0
      end if
      waitms 500
   end if

end Sub

'����������εı���
BianMa:
Data &H80 , &HA0 , &H20 , &H60
Data &H40 , &H50 , &H10 , &H90