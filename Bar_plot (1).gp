set terminal postscript eps enhanced "Helvetica" 60
set grid y
set style data histogram
set style histogram cluster gap 2
set style fill solid border -1
set boxwidth 0.8
set xtics rotate by 0 font "Helvetica, 60"
set ylabel 'Total distance between sellers'
set key autotitle columnheader
set key left
set key font "47"
set key spacing "1.2"
set term post size 14,12
#set term eps size 800,400
set xlabel 'No. of clusters'
set yrange[0:100000]

set output 'new.eps'
set title "Total Distance Comparison"
plot "plot_data.txt" using 2:xticlabels(1) title "With cluster" lt rgb "yellow",\
	 "" using 3:xticlabels(1) title "without cluster" lt rgb "violet"


