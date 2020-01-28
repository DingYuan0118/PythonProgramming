import matplotlib.pyplot as plt
import time

#start = time.time()
#squares = []
#input_values = []
#for i in range(1, 6):
#	squares.append(i * i)
#	input_values.append(i)
#	
#plt.scatter(input_values, squares, s=200)
##设置图表标题，并给坐标轴加上标签
#plt.title("Square Numbers", fontsize=24)
#plt.xlabel("Value", fontsize=14)
#plt.ylabel("Square of value", fontsize=14)
#
##设置刻度标记的大小
#plt.tick_params(axis='both', which='major', labelsize=14)
#plt.show()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
            edgecolor='none', s=4)
#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png')
plt.show()
