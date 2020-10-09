import numpy as np

def f(x):
	y=np.log( np.exp(1/(np.sin(x)+1)) / (5/4+1/x**15) )/np.log(1+x*x)
	return y
	
print(f(1))
print(f(10))
print(f(1000))


