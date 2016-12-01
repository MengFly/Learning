$regfile = "m16def.dat"
$crystal = 12000000

Config Porta.3 = Output
Config Porta.4 = Output
Config Portc = Output

Dim A As Integer
Do

 '输出I
 For A = 0 To 800
     '输出I
    Porta.3 = 1
    Portc = &B00000110
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11110111
    Porta.4 = 0

    Waitms 1

 Next

 '输出Love
 For A = 0 To 200
    '输出L
    Porta.3 = 1
    Portc = &B00111000
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11101111
    Porta.4 = 0

    Waitms 1

    '输出o
    Porta.3 = 1
    Portc = &B00111111
    Porta.3 = 0


    Porta.4 = 1
    Portc = &B11110111
    Porta.4 = 0

    Waitms 1

    '输出V
    Porta.3 = 1
    Portc = &B00111110
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11111011
    Porta.4 = 0

    Waitms 1

    '输出E
    Porta.3 = 1
    Portc = &B01111001
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11111101
    Porta.4 = 0

    Waitms 1

 Next

 '输出YOU
 For A = 0 To 600

    '输出Y
    Porta.3 = 1
    Portc = &B01101110
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11110111
    Porta.4 = 0

    Waitms 1

    '输出O
    Porta.3 = 1
    Portc = &B00111111
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11111011
    Porta.4 = 0

    Waitms 1

    '输出U
    Porta.3 = 1
    Portc = &B00111110
    Porta.3 = 0

    Porta.4 = 1
    Portc = &B11111101
    Porta.4 = 0

    Waitms 1


 Next

Loop

End