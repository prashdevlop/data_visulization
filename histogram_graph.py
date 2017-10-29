#Simple Histogram Graph
from matplotlib import pyplot as plt


x=[1,2,3,5,3,6,7,3,1,4,5,6,7,3,2,4,5,4,6,7,9,8,4,7,5]
y=[1,2,3,4,5,6,7,8,9]

plt.hist(x,y,histtype='bar',rwidth=0.5)

#graph title and x and y axis
plt.title("Histogram Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#legend is used to show graph labels
plt.legend()

plt.show()
