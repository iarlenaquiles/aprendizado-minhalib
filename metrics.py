import numpy as np 

def mse(y_true, y_pred):
	return np.sum((y_true-y_pred)**2)/len(y_true)
	

def rmse(y_true, y_pred):
	return np.sqrt(mse(y_true, y_pred))


def mae(y_true, y_pred):
	y = np.absolute(y_true)
	y_p = np.absolute(y_pred)

	return np.sum(np.absolute(y - y_p))/len(y_true)
