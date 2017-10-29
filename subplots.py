#Simple Line Graph
from matplotlib import pyplot as plt

#graph 1
x1=[1,2,3]
y1=[9,3,2]

plt.subplot(121)

#graph 1
plt.plot(x1,y1,label="graph 1")

#graph title and x and y axis
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

###########################

#Simple Scattter Graph

#graph 2
x2=[4,5,6]
y2=[4,1,7]

plt.subplot(122)

#graph 2
plt.scatter(x2,y2,label="graph 2")

#graph title and x and y axis
plt.title("Simple Scatter Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#legend is used to show graph labels
plt.legend()

plt.show()

