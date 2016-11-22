print 'hello'
def method(a, b):
	return a + b
class MyClass(object):
	"""docstring for MyClass"""
	def __init__(self,a,b,c):
		super(MyClass, self).__init__()
		self.a = a
		self.b = b
		self.c = c

m = MyClass(1, 3, 4)
		