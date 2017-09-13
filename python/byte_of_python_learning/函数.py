def say(message, times=1):
             print(message * times)

say('Hello')
say('World', 5)

def func(a, b=5, c=10):
             print(' a is ', a, ' and b is ', b, ' and c is ', c)

func(3, 7)
func(25, c=39)
func(c=34, a=1)


# 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
# 类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。
def total(a=5, *numbers, **phonebook):
             '''这个函数用来获取函数的各种参数
             其中，
             当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
             类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。
             '''
             print('a', a)

             #遍历元组中的所有项目
             for single_item in numbers:
                          print('single_item ', single_item)

             # 遍历字典中的所有项目
             for first_part, second_part in phonebook.items():
                          print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


print(total.__doc__)
