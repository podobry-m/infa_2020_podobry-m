import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p1, v1 = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)
p_f1 = np.poly1d(p1)
p_f2 = np.poly1d(p2)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.plot(x,p_f1(x))
plt.plot(x,p_f2(x))
plt.show()

