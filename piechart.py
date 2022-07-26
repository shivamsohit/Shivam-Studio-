#A SIMPLE PIE CHART#

from matplotlib.pyplot import*

title('SHIVA + M STUDIO\n\nA SIMPLE PIE CHART')
x=[10,30,40,20]
y=['Kunal','Sagar','Deepak siwach','Dhananjay']
d=[0,0,0.1,0]

pie(x,labels=y,autopct='%1.1f%%',explode=d)
savefig('matplotlib 7.pdf')
show()