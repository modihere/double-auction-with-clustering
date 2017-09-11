import Gnuplot
f=open("plotter.txt","r")
def plotter():
	data1=list()
	j=0
	for line in f:
		data1.append([])
		data1[j] = [float(i) for i in line.split()]
		j+=1
	for i in data1:
		print(i)
	f.close()
	gp1=Gnuplot.Gnuplot(persist =1)
	gp1('set terminal x11 size 500,500')
	gp1('set pointsize 3')
	gp1('set boxwidth 0.5')
	gp1 ('set style fill solid')
	gp1('set font "Times-Roman, 30"')
	gp1('set xlabel "x-axis"')
	gp1('set ylabel "y-axis"')
	gp1('set xrange [0:10]')
	gp1('set yrange [0:100000]')
	plot1 = Gnuplot.PlotItems.Data(data1, with_="boxes" ,title='best allocation ')
	gp1.plot(plot1)
	epsFilename ='t.eps'
	gp1.hardcopy(epsFilename, terminal = 'postscript',color=1)
	gp1.reset()
plotter()
f.close()