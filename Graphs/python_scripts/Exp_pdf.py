import matplotlib.pyplot as plt
import numpy as np
import math
sigma1=2
sigma2=1
sigma3=0.5
sigma4=0.2
x=np.arange(0.1,4,0.02)
y1=[math.exp(-x1/sigma1)/sigma1 for x1 in x]
y2=[math.exp(-x1/sigma2)/sigma2 for x1 in x]
y3=[math.exp(-x1/sigma3)/sigma3 for x1 in x]
y4=[math.exp(-x1/sigma4)/sigma4 for x1 in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['sigma=2', 'sigma=1', 'sigma=0.5', 'sigma=0.2'], loc='upper left')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("p.d.f for exponential distribution")
plt.show()