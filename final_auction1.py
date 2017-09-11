import re
from k_means import *
def takeThirdandFourth(e):
    return e[2],e[4],e[5]
def takefirst(e):
	return e[0]

f=open("seller_coordinates.txt","w")

def allocator(sellerdata,time_slot,cluster,j,buyerdata):#the counter takes the number of element in each cluster
	sellprice=list()
	sellerx1=list()
	sellery1=list()
	buyprice=list()
	count=0
	#take the buyer prices
	for i in range(10):
		buyprice.append(buyerdata[i][0])
	print (buyprice)
	#take the seller prices
	for size in range (cluster):
		print("\nFOR CLUSTER ", size)
		
		for i in range (1,4):
			print("\nIN THE TIME SLOT OF",time_slot[i],": 00 HOURS\n")
			count=0
			for k in range (j):
				if sellerdata[k][2]==size:
					if sellerdata[k][4]<=time_slot[i] and sellerdata[k][4]>time_slot[i-1]:
						sellprice.insert(count,sellerdata[k][3])
						sellerx1.insert(count,sellerdata[k][0])
						sellery1.insert(count,sellerdata[k][1])
						count+=1

			sellerx=[x for _,x in sorted(zip(sellprice,sellerx1))]
			sellery=[x for _,x in sorted(zip(sellprice,sellery1))]
			sellprice.sort()
			print (sellprice)
			print (sellerx)
			print (sellery)
			doubleauction(sellprice,buyprice,sellerx,sellery)
			del sellprice[:]
			del sellery[:]
			del sellerx[:]


def doubleauction(sellprice,buyprice,sellerx,sellery):
	newsellprice=list()
	newbuyprice=list()
	newsellerx=list()
	newsellery=list()
	count=0
	newcount=0
	breakindex=0
	#if number of sellers are less than the number of buyers.
	if len(sellprice)<= len(buyprice):
		print("\nIN IF PART\n")
		length=len(sellprice)
		#print(length)
		for i in range (length):
			if sellprice[i]>buyprice[i]:
				breakindex=i
				
				break
			else:
				breakindex=i
		
		print("\nthe breakindex is",breakindex,"\n")
		print("\nfor all buyers' calcuations:\n")
		#for all buyer calculations:
		if length>2:
			for i in range(1,breakindex):
				newsellprice.append(sellprice[i])
				count+=1
			newsellprice.append(sellprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			newsellprice.insert(0,0)
			count+=1
			print(newsellprice)
		else:#when number of elements is less than or equal to 2.
			for i in range(breakindex):
				newsellprice.append(sellprice[i])
				count+=1
			newsellprice.append(sellprice[breakindex])
			print(newsellprice)

		for k in range(breakindex+1):
			
			for i in range (k):
				newbuyprice.append(buyprice[i])
				newcount+=1
			newbuyprice.insert(newcount,100000)
			for i in range (k+1,breakindex+1):
				newbuyprice.append(buyprice[i])
				newcount+=1
			if breakindex==newcount and newbuyprice[newcount]==100000:
				newcount-=1
				count-=1
			elif breakindex==newcount:
				dummy=0
			else:
				newbuyprice.append(buyprice[breakindex])
			
			if k<breakindex or breakindex==length-1:
				print(newbuyprice)
				avgprice=(newbuyprice[newcount]+newsellprice[count])/2
				print(" the price for the buyer with",buyprice[k],"has to pay",avgprice)
			del newbuyprice[:]
			newcount=0
		count=0
		newcount=0

		print("\nthe breakindex is",breakindex,"\n")
		print("\nfor all seller calcualtions:\n")
		#for all seller calculations: 
		del newsellprice[:]
		if length>2:
			for i in range(1,breakindex):
				newbuyprice.append(buyprice[i])
				count+=1
			newbuyprice.append(buyprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			newbuyprice.insert(0,100000)
			count+=1
			print(newbuyprice)
		else:
			for i in range(breakindex):
				newbuyprice.append(buyprice[i])
				count+=1
			newbuyprice.append(buyprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			print(newbuyprice)

		for k in range(breakindex+1):
			
			for i in range (k):
				newsellprice.append(sellprice[i])
				newcount+=1
			newsellprice.insert(newcount,0)
			for i in range (k+1,breakindex+1):
				newsellprice.append(sellprice[i])
				newcount+=1
			if breakindex==newcount and newsellprice[newcount]==0:
				newcount-=1
				count-=1
			elif breakindex==newcount:
				dummy=0
			else:
				newsellprice.append(sellprice[breakindex])
			
			if k<breakindex or breakindex==length-1:
				print(newsellprice)
				avgprice=(newbuyprice[newcount]+newsellprice[count])/2
				f.write(str(sellerx[k])+" "+str(sellery[k])+"\n")
				print(" the price for the seller with",sellprice[k],"and coordinates",sellerx[k]," ",sellery[k],"will receive",avgprice)
			del newsellprice[:]
			newcount=0
		count=0
		newcount=0




	#if number of buyers are less than the number of sellers.
	else:
		print("\nIN ELSE PART\n")
		length=len(buyprice)
		#print(length)
		for i in range (length):
			if sellprice[i]>buyprice[i]:
				breakindex=i
				
				break
			else:
				breakindex=i
		
		print("\nthe breakindex is",breakindex,"\n")
		print("\nfor all buyers' calcuations:\n")
		#for all buyer calculations:
		if length>2:
			for i in range(1,breakindex):
				newsellprice.append(sellprice[i])
				count+=1
			newsellprice.append(sellprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			newsellprice.insert(0,0)
			count+=1
			print(newsellprice)
		else:
			for i in range(breakindex):
				newsellprice.append(sellprice[i])
				count+=1
			newsellprice.append(sellprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			print(newsellprice)

		for k in range(breakindex+1):
			
			for i in range (k):
				newbuyprice.append(buyprice[i])
				newcount+=1
			newbuyprice.insert(newcount,100000)
			for i in range (k+1,breakindex+1):
				newbuyprice.append(buyprice[i])
				newcount+=1
			if breakindex==newcount and newbuyprice[newcount]==100000:
				newcount-=1
				count-=1
			elif breakindex==newcount:
				dummy=0
			else:
				newbuyprice.append(buyprice[breakindex])
			
			if k<breakindex or breakindex==length-1:
				print(newbuyprice)
				avgprice=(newbuyprice[newcount]+newsellprice[count])/2
				print(" the price for the buyer with",buyprice[k],"has to pay",avgprice)
			del newbuyprice[:]
			newcount=0
		count=0
		newcount=0

		print("\nthe breakindex is",breakindex,"\n")
		print("\nfor all seller calcualtions:\n")
		#for all seller calculations: 
		del newsellprice[:]
		if length>2:
			for i in range(1,breakindex):
				newbuyprice.append(buyprice[i])
				count+=1
			newbuyprice.append(buyprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			newbuyprice.insert(0,100000)
			count+=1
			print(newbuyprice)
		else:
			for i in range(breakindex):
				newbuyprice.append(buyprice[i])
				count+=1
			newbuyprice.append(buyprice[breakindex])#taking the extra element for removal of elements while applying the algo.
			print(newbuyprice)

		for k in range(breakindex+1):
			
			for i in range (k):
				newsellprice.append(sellprice[i])
				newcount+=1
			newsellprice.insert(newcount,0)
			for i in range (k+1,breakindex+1):
				newsellprice.append(sellprice[i])
				newcount+=1
			if breakindex==newcount and newsellprice[newcount]==0:
				newcount-=1
				count-=1
			elif breakindex==newcount:
				dummy=0
			else:
				newsellprice.append(sellprice[breakindex])
			
			if k<breakindex or breakindex==length-1:
				print(newsellprice)
				avgprice=(newbuyprice[newcount]+newsellprice[count])/2
				f.write(str(sellerx[k])+" "+str(sellery[k])+"\n")
				print(" the price for the seller with",sellprice[k],"and coordinates",sellerx[k]," ",sellery[k],"will receive",avgprice)
			del newsellprice[:]
			newcount=0
		count=0
		newcount=0




					
def pricecalculator():
	main()
	time_slot=[8,10,13,15,17]
	#activeagents=list()
	sellerdata=list()
	buyerdata=list()
	#sellerprice=list()
	#avgbuysell=list()
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
	
	allocator(sellerdata,time_slot,cluster,j,buyerdata)
pricecalculator()
f.close()