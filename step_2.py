import math
from step_0 import *

def calc():
	f=open("seller_coordinates.txt","r")
	f1=open("plotter.txt","a+")
	coordinates=list()
	coordinate_sum=0
	j=0
	for line in f:
		coordinates.append([])
		coordinates[j]=[float(i) for i in line.split()]
		j+=1
	print(coordinates)
	print (j)
	for i in range (j):
		for k in range (i,j):
			dist = math.sqrt( (coordinates[k][1] - coordinates[i][1])**2 + (coordinates[k][0] - coordinates[i][0])**2 )
			print (dist)
			coordinate_sum+=dist
			
	print(coordinate_sum)
	f1.write(str(coordinate_sum)+"\n")
#calc()
	f.close()
	f1.close()
