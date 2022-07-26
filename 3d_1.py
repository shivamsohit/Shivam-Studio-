from matplotlib.pyplot import*
from mpl_toolkits.mplot3d import Axes3D
from math import*
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[4,8,12,16,20]

#fig = figure(figsize=(4,4))
ax=axes(projection='3d')
ax.scatter(x,y,z,s=600)#s=size and poinys are made by this
ax.set_title('Shiva+m Studio')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')


ax.plot(x,y,z,lw=6,color='green',linestyle='dotted')#Line is drawn by this

show()