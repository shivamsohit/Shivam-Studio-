from matplotlib.pyplot import*
from numpy import*

x=arange(1,20,1)
y=arange(2,40,2)
a=arange(40,20,-2)
b=arange(20,40,2)


subplot(2,1,1)
plot(x,y)

subplot(2,1,2)
plot(b,a)
savefig("/storage/emulated/0/emulated/Sd card/Results/matplotlib 10.pdf")



show()