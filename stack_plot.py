#Simple Scattter Graph
from matplotlib import pyplot as plt

#Days
d=[1,2,3,4,5]


sleeping=[7,5,9,6,7]
eating=[2,3,4,3,2]
playing=[2,3,4,1,3]


plt.plot([],[],color='m',label="sleeping",linewidth=5)
plt.plot([],[],color='c',label="eating",linewidth=5)
plt.plot([],[],color='r',label="playing",linewidth=5)

#ploting stack graph
plt.stackplot(d,sleeping,eating,playing,colors=['m','c','r'])


#graph title and x and y axis
plt.title("Simple  Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#legend is used to show graph labels
plt.legend()

plt.show()
