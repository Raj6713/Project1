
#This graph will plot the hazard function for the exponential distribution and will show it on the screen.
import matplotlib.pyplot as plt 
import numpy as np 
import math
x=np.arange(0,10,0.1)
sigma1=2
sigma2=1
sigma3=0.5
sigma4=0.2
y1=[(math.exp(-x1/sigma1)/sigma1)/(math.exp(-x1/sigma1)) for x1 in x]
y2=[(math.exp(-x1/sigma2)/sigma2)/(math.exp(-x1/sigma2)) for x1 in x]
y3=[(math.exp(-x1/sigma3)/sigma3)/(math.exp(-x1/sigma3)) for x1 in x]
y4=[(math.exp(-x1/sigma4)/sigma4)/(math.exp(-x1/sigma4)) for x1 in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['sigma1=2','sigma2=1','sigma3=0.5'],loc='upper left')
plt.xlabel("x-axis")
plt.ylabel("$h(x)=f(x)/s(x)$")
plt.title("Hazard function for exponential distribution")
plt.show()