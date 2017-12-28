def sigmoid(z):
	return 1/(1+np.exp(-z))

def sigmoid_derivative(z):
	return sigmoid(z)*(1-sigmoid(z))


def tanh(z):
	return np.tanh(z)


def tanh_derivative(z):
	return 1- tanh(z)*tanh(z)

def ReLU(z):
	return np.where(z>0, z, 0)

def ReLU_derivative(z):
	return np.where(z>=0, 1, 0)

def lost_funcion(y, y_):
	return -(y*np.log(y_) + (1-y)*np.log(1-y_))
