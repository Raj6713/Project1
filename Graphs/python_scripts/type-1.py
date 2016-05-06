
#Write a program which will find the mean for the type-1 censored data
import matplotlib.pyplot as plt 
import numpy as np 
import math
datapoints=int(input("Enter total no of datapoints: "))
data=[]
for i in range(datapoints):
	num=float(input("Enter data "))
	data.append(num)
T=float(input("Enter the censorering time: "))
failure_count=0
sum_ti=0
for i in range(datapoints):
	if(data[i]<T):
		sum_ti+=data[i]
		failure_count+=1

#mean estimate of the type-1 censored data
lambda_bar=failure_count/(sum_ti+(datapoints-failure_count)*T)
print("The mean estimate for censored Type-1 exponential data is given by "+str(lambda_bar))
