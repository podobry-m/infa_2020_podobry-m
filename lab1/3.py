import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)
plt.plot(x, np.log(x*x+1)/np.log(1+np.tan(1/(1+np.sin(x)**2)))*np.exp(-abs(x)/10))
plt.grid(True)
plt.show()

