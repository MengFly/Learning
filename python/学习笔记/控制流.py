# if
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
             print('Congratulations, you guessd it')
             print(' (But you do not win any prizes!)')
elif guess < number:
             print('No, it is a little higher than that')
else :
             print('No, it is a little lower than that')

print('Done')

#Python 中不存在 switch 语句。你可以通过使用 if..elif..else 语句来实现同样的事情（在某些情况下，使用一部字典能够更快速地完成）


# while
number = 23
running = True

while running:
             guess = int(input('Enter an integer:'))

             if guess == number:
                          print('Congratulations, you guessd it')
                          print(' (But you do not win any prizes!)')
                          running = False
             elif guess < number:
                          print('No, it is a little higher than that')
             else :
                          print('No, it is a little lower than that')
#你可以在 while 循环中使用 else 从句
else:
             print('The while loop is over')

print('Done')


# for

# range的第三个参数就是它递增的跨度
for i in range(1, 5):
             print(i, end=' ')
else:
             print('The for loop is over')











