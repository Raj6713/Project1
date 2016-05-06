

#Write a program which will find out the the maximum likelihood estimator of the type-2 censored data and will show it on the screen
#input Block for the data 
import matplotlib.pyplot as plt 
import numpy as np 
import math 
datapoints=int(input("Enter the  number of data points: "))
r=int(input("Enter the lower censoring bound(r<n) and(r<s): "))
s=int(input("Enter the upper censoring bound(s>r)and(s<n): "))
data=[]
for i in range(datapoints):
	num=float(input("Enter data: "))
	data.append(num)

#inital guess is taken to be the true mean of the quantity of the following given.
initial_guess=0
for i in range(datapoints):
	initial_guess+=data[i]
initial_guess=datapoints/initial_guess
#block to sort data
for i in range(datapoints):
	for j in range(i+1,datapoints):
		if(data[i]>data[j]):
			a=data[i]
			data[i]=data[j]
			data[j]=a
tr=data[r]
ts=data[s]
sum_xi=0
for i in range(r,s+1):
 	sum_xi+=data[i]
error_limit=1e-5 
 #simulation point
k=0
k+=1
x0=initial_guess
initial_guess=(s-r+1)*(math.exp(x0*tr)-1)/((sum_xi+(datapoints-s)*ts)*(math.exp(x0*tr)-1)-(r-1)*tr)
print("%d \t\t %.5f",k,intial_guess)
while(math.fabs(x0-initial_guess)>error_limit):
	k+=1
	x0=intial_guess
	initial_guess=(s-r+1)*(math.exp(x0*tr)-1)/((sum_xi+(datapoints-s)*ts)*(math.exp(x0*tr)-1)-(r-1)*tr)
	print("%d \t\t %.5f",k,initial_guess)
print("Value of the root is %.4f",inital_guess)





