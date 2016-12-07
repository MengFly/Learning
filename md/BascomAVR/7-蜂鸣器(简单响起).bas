$regfile = "m16def.dat"

$crystal = 8000000

Config portb.3 = output

'蜂鸣器响应该是边缘触发,所以在portB.3电压变化的时候才会响
do
   portb.3 = 0
   waitms 5
   portb.3 = 1
   waitms 5
loop

End
