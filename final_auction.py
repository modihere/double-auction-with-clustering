import re
from k_means import *
def takeThirdandFourth(e):
    return e[2],e[4],e[5]
def takefirst(e):
	return e[0]

def pricecalculator():
	main()
	time_slot=[10,11,13,14,15,17]
	activeagents=list()
	sellerdata=list()
	buyerdata=list()
	sellerprice=list()
	avgbuysell=list()
	cluster=5 #num_clusters
	seller=open("pointer.txt","r")
	buyer=open("buyer.txt","r")

	
	#read the seller data from the file seller.txt and sort the seller prices in ascending order.
	j=0
	for line in seller:
		sellerdata.append([])
		#for x in line.split():
		sellerdata[j] = re.findall(r"[-+]?\d*\.\d+|\d+",line)
		j+=1
	for sell in range (j):
		for sell1 in range(2,7):
			sellerdata[sell][sell1]=int(sellerdata[sell][sell1])
	sellerdata.sort(key=takeThirdandFourth)
	for sell in sellerdata:
		print(sell)
	#for sell in range (j):
		#print(sellerprice[sell])

	#read the buyer data from the file buyer.txt and sort them in descending order.

	buyercounter=0
	for line in buyer:
		buyerdata.append([])
		buyerdata[buyercounter]=[int(k) for k in line.split()]
		buyercounter+=1
	buyerdata.sort(key=takefirst,reverse=True)
	print("\nthe price offered by the buyers in descending order are: \n")
	print(buyerdata)
	print("\n")

	#keep the seller price of each seller of each cluster in sellerprice list.
	
	'''for i in range (j):
		for k in range (5):
			if(sellerdata[i][4]==time_slot[k]):
				activeagents.insert(i,sellerdata[i][4])

'''

#starting from cluster 0
	counter=0
	for size in range (cluster):
	

		#search over the time slots
		for i in range (j):
			
			for k in range(5):
				#change append to insert while running the final code so aas to avoid some bugs.
				if size == sellerdata[i][2] and sellerdata[i][4] >= time_slot[k] and sellerdata[i][5]<=time_slot[k+1]:
					sellerprice.append([])
					sellerprice[counter].append(sellerdata[i][3])
					sellerprice[counter].append(sellerdata[i][6])
					sellerprice[counter].append(sellerdata[i][2])
					counter+=1	
		
	print(sellerprice)
pricecalculator()