import re
#from k_means import *
def takeThirdandFourth(e):
    return e[2],e[3]
def pricecalculator():    
	#main()
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
	print("\nthe price offered by the buyers in descending order are: \n")
	for m in range (buyercounter):
		print (buyerdata[m][0])

	#keep the seller price of each seller of each cluster in sellerprice list.
	for size in range (cluster):
		counter=0
		#sellerprice[:]
		print("\nIn cluster",size,"the following transactions take place:\n")
		print("\nprice wanted by the sellers in ascending order are:\n")
		for i in range (j):
			if size==sellerdata[i][2]:
				sellerprice.insert(counter,sellerdata[i][3])
				print(sellerprice[counter])
				counter+=1
		print("\nThe compatible buyers and sellers are listed below:\n\nIf no data is listed then the buyers and sellers are not compatible\n")
		if(buyercounter<counter):
			for i in range (buyercounter):
				if buyerdata[i][0] >= sellerprice[i]:
					print(buyerdata[i][0],sellerprice[i])
					avgbuysell=(buyerdata[i][0]+sellerprice[i])/2
					utilofbuyer=buyerdata[i][0]-avgbuysell
					utilofseller=avgbuysell-sellerprice[i]
					print("Seller and buyer number",i,"with incentives of seller and of buyer being",utilofbuyer,"\n")
		else:
			for i in range (counter):
				if buyerdata[i][0] >= sellerprice[i]:
					print(buyerdata[i][0],sellerprice[i])
					avgbuysell=(buyerdata[i][0]+sellerprice[i])/2
					utilofbuyer=buyerdata[i][0]-avgbuysell
					utilofseller=avgbuysell-sellerprice[i]
					print("Seller and buyer number",i,"with incentives of seller and of buyer being",utilofbuyer,"\n")

pricecalculator()