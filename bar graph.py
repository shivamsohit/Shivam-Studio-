#A SIMPLE BAR GRAPH#


from matplotlib.pyplot import*

title("SHIVA + M STUDIO\n\nA SIMPLE BAR GRAPH")
x=[10,20,30,40,50,60]
y=[20,40,60,80,100,120]
bar(x,y,color=['r','g','b','y','m','c'],width=[1,1.5,2,2.5,3,3.5])
xlabel('Some values')
ylabel('Douled values')

legend(loc='upper left')
savefig('/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/matplotlib 5.pdf')
show()
####






