
#Write a program which will create the graph for the mean residual life function and will show it on the screen.
import matplotlib.pyplot as plt 
import numpy as np 
import math 
x=np.arange(1e-10,10,0.1)
sigma1=2
sigma2=1
sigma3=0.5 
sigma4=0.2
y1=[(sigma1*math.exp(-xi/sigma1))/(math.exp(-xi/sigma1)) for xi in x]
y2=[(sigma2*math.exp(-xi/sigma2))/(math.exp(-xi/sigma2)) for xi in x]
y3=[(sigma3*math.exp(-xi/sigma3))/(math.exp(-xi/sigma3)) for xi in x]
y4=[(sigma4*math.exp(-xi/sigma4))/(math.exp(-xi/sigma4)) for xi in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['sigma=2','sigma=1','sigma=0.5','sigma4=0.2'],loc='upper left')
plt.xlabel('X-axis')
plt.ylabel('$mrl(x)=\sigma*exp(-x/\sigma)/exp(-x/\sigma)$')
plt.title('mean residual life for exponential distribution')
plt.show()