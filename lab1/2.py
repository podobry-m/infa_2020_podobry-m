import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-4, 4, 0.01)
plt.plot(x, x*x-x-6)
plt.grid(True)
plt.show()

