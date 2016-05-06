
#program to generate the cumulative distribution function for the exponential distribution function 
import matplotlib.pyplot as plt 
import numpy as np 
import math
x=np.arange(0,10,0.02)
sigma1=2
sigma2=1
sigma3=0.5
sigma4=0.2
y1=[(1-math.exp(-xi/sigma1)) for xi in x]
y2=[(1-math.exp(-xi/sigma2)) for xi in x]
y3=[(1-math.exp(-xi/sigma3)) for xi in x]
y4=[(1-math.exp(-xi/sigma4)) for xi in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['sigma=2', 'sigma=1', 'sigma=0.5', 'sigma=0.2'], loc='upper left')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("C.D.F for exponential distribution")
plt.show()