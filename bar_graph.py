#Simple Bar Graph
from matplotlib import pyplot as plt

#using style option
from matplotlib import style

#graph 1
x1=[1,2,3]
y1=[9,3,2]

#graph 2
x2=[4,5,6]
y2=[4,1,7]

#style.use('ggplot')

#graph 1
plt.bar(x1,y1,label="Data 1")
#graph 2
plt.bar(x2,y2,label="Data 2")

#graph title and x and y axis
plt.title("Simple Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#legend is used to show graph labels
plt.legend()

plt.show()
