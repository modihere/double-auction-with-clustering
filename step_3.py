from step_0 import *
f=open("plotter.txt","r")
f1=open("plot_data.txt","a+")
avg_list=list()
for line in f:
	avg_list.append(float(line))
average=sum(avg_list)/len(avg_list)

print (avg_list)
print(average)
f1.write(str(num_clusters)+" "+str(average)+"\n")
f.close()
f1.close()
