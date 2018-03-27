import numpy as np

class SimpleLinearRegression:
            
    def __isNumpyArray(self, arr):
        return type(arr) == np.ndarray
    
    def fit(self, x, y):
        if self.__isNumpyArray(x):
            x = x[:, 0]
            
        b1 = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2) 
        b0 = np.mean(y) - b1 * np.mean(x)
        print ('b0={}, b1={}'.format(b0, b1))
        
        self.b0, self.b1 = b0, b1
    
    def predict(self, x):
        if self.__isNumpyArray(x):
            x = x[:, 0]
            
        print('b0={}, b1={}'.format(self.b0, self.b1))
        
        return self.b0 + self.b1 * x