$regfile = "m16def.dat"

$crystal = 8000000

Config portb.3 = output

'��������Ӧ���Ǳ�Ե����,������portB.3��ѹ�仯��ʱ��Ż���
do
   portb.3 = 0
   waitms 5
   portb.3 = 1
   waitms 5
loop

End
