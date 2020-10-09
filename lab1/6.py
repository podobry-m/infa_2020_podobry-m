import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 3, 0.01)
s=0
for n in range (100):
	s+=0.5**n*np.cos(3**n*np.pi*x)
plt.plot(x, s)
plt.grid(True)
plt.show()

