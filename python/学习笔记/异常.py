try :
             text = input('Enter something:')
except EOFError:
             print('Why did you an EOF on me?')
except KeyboardInterrupt:
             print('You cancelld the operation.')
else :
             print('You enterd {}'.format(text))


class ShortInputException(Exception):
             '''A user-defind exception class'''
             def __init__(self, length, atleast):
                          Exception.__init__(self)
                          self.length = length
                          self.atleast = atleast

try:
             text = input('Enter something:')
             if len(text) < 3:
                          raise ShortInputException(len(text), 3)
except EOFError:
             print('Why did you an EOF on me?')
except KeyboardInterrupt:
             print('You cancelld the operation.')
except ShortInputException as ex:
             print('ShortInputException The input was {0} long, excepted atleast {1}'.format(ex.length, ex.atleast))
else:
             print('You enterd {}'.format(text))


import time
try:
             f = open('shoplist.data', 'rb')
             while True:
                          line = f.readline()
                          if len(line) == 0:
                                       break
                          print(line, end = " ")
                          time.sleep(2)
except KeyboardInterrupt:
             print('! you cancelled the reading from the file.')
except FileNotFoundError:
             print('File not found')
finally:
             if 'f' in locals().keys():
                          f.close()
                          print('file closed')
             print('(Cleaning up: close the file')


with open('shoplist.data', 'rb') as f:
             for line in f:
                          print(line, end='')
