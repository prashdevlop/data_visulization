#Simple Line Graph
from matplotlib import pyplot as plt

#using style option
from matplotlib import style

#graph 1
x1=[1,2,3]
y1=[9,3,2]
#graph 2
x2=[3,5,6]
y2=[4,1,7]

style.use('ggplot')
#graph 1
plt.plot(x1,y1,label="graph 1")
#graph 2
plt.plot(x2,y2,label="graph 2")

#graph title and x and y axis
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#legend is used to show graph labels
plt.legend()

plt.show()
