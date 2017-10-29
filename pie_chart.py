#Simple Histogram Graph
from matplotlib import pyplot as plt


slices=[2,8,3,6]
activities=['reading','sleeping','eating','playing']

#how to extract eating by explode is shown below and how to add auto percentage
plt.pie(slices,labels=activities,shadow=True,explode=(0,0,0.1,0),autopct='%1.2f%%')


#graph title and x and y axis
plt.title("Pie Chart")

plt.show()
