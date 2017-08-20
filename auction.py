import re
from k_means import *
def takeThirdandFourth(e):
    return e[2],e[3]
def pricecalculator():    
	main()
	sellerdata=list()
	buyerdata=list()
	sellerprice=list()
	avgbuysell=list()
	cluster=num_clusters
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
		for sell1 in range(2,5):
			sellerdata[sell][sell1]=int(sellerdata[sell][sell1])
	sellerdata.sort(key=takeThirdandFourth)
	for sell in sellerdata:
		print(sell)
	#for sell in range (j):
		#print(sellerprice[sell])

	#read the buyer data from the file buyer.txt and sort them in descending order.

	buyercounter=0
	for line in buyer:
		buyerdata.append([int(k) for k in line.split()])
		buyercounter+=1
	buyerdata.sort(reverse=True)
	for m in range (buyercounter):
		print (buyerdata[m])

	#keep the seller price of each seller of each cluster in sellerprice list.
	for size in range (cluster):
		counter=0
		print("\nIn cluster",size,"the following transactions take place:\n")
		for i in range (j):
			if size==sellerdata[i][2]:
				sellerprice.append(sellerdata[i][3])
				counter+=1
		for i in range (buyercounter):
			if buyerdata[i][0]>=sellerprice[i]:
				avgbuysell=(buyerdata[i][0]+sellerprice[i])/2
				utilofbuyer=buyerdata[i][0]-avgbuysell
				utilofseller=avgbuysell-sellerprice[i]
				print("Seller and buyer number",i,"with incentives of seller and of buyer being",utilofbuyer,"\n")
		sellerprice[:]
pricecalculator()