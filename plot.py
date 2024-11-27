import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6.1, 0.1)
a = 1 # определение a
b = 1 #  определение b
y1 = np.sin((a + b)**2 * np.pi * t) 

plt.plot(t, y1, 'b-')
plt.plot(t, y1, 'b*')
plt.show()