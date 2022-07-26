#A SIMPLE LINE GRAPH#


from matplotlib.pyplot import*

title("SHIVA + M STUDIO\n\nA SIMPLE LINE GRAPH")
x=[10,20,30,40,50,60]
y=[20,40,60,80,100,120]
plot(x,y,'blue',linewidth=2,linestyle='dashed',marker='d',markersize=25,markeredgecolor='black')
xlabel('Some values')
ylabel('Douled values')

#legend(loc='upper left')
savefig('matplotlib 1.pdf')
show()





		