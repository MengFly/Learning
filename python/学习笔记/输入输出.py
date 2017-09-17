# 用户输入
def reverse(text):
             return text[::-1]

def is_palindrome(text):
             return text == reverse(text)

something = input("Enter text: ")
if(is_palindrome(something)):
             print("Yes, it is a palindrome")
else:
             print("No,it is not a palindrome")


#pickle 模块
#Python 提供了一个叫做 pickle 的标准模块，使用该模块你可以将任意对象存储在
#文件中，之后你又可以将其完整地取出来。这被称为持久地存储对象。

import pickle
# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

#write to the file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

# read back form the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)


























