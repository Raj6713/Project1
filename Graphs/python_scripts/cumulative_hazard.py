
#write a program which will print the cumulative hazard function
import matplotlib.pyplot as plt 
import numpy as np 
import math
x=np.arange(1e-10,10,0.1)
sigma1=2
sigma2=1
sigma3=0.5
sigma4=0.2
y1=[(-math.log(math.exp(-x1/sigma1))) for x1 in x]
y2=[(-math.log(math.exp(-x1/sigma2))) for x1 in x]
y3=[(-math.log(math.exp(-x1/sigma3))) for x1 in x]
y4=[(-math.log(math.exp(-x1/sigma4))) for x1 in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.legend(['sigma1=2','sigma2=1','sigma3=0.5','sigma4=0.2'],loc='upper left')
plt.xlabel("X-axis")
plt.ylabel("$H(x)=-ln(s(x))$")
plt.title("Cumulative hazard function for exponential distribution")
plt.show()
