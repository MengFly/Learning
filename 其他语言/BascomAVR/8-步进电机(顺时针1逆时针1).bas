$regfile = "m16def.dat"
$crystal = 8000000

Config Portd = output

Dim B(8) As Byte                                            '���ڴ洢����������εı��������
Dim I as Byte                                               '���ڴ洢�����������λ��'
Dim X as integer                                            '�����������ѭ������'                           

'�����ݶ�������
restore BianMa
for i = 1 to 8
   Read B(i)
next

Do
   '˳ʱ��
   gosub ShunShiZhen
   waitms 500
   '��ʱ��
   gosub NiShiZhen
   waitms 500
Loop


End

'˳ʱ����ת
ShunShiZhen:
I = 1
For X = 1 to 4096
   portd = B(i)
   incr i
   waitms 1
   if i = 9 then i = 1
Next
Return

'��ʱ����ת
NiShiZhen:
I = 8
for x = 1 to 4096
   portd = B(i)
   decr i
   waitms 1
   if i = 0 then i = 8
Next
Return


'����������εı���
BianMa:
Data &H80 , &HA0 , &H20 , &H60
Data &H40 , &H50 , &H10 , &H90