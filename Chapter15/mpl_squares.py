import matplotlib.pyplot as plt
import time

start = time.time()
squares = []
input_values = []
for i in range(1, 6):
	squares.append(i * i)
	input_values.append(i)
	

plt.plot(input_values, squares, linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
end = time.time()
print("Spend {} seconds.".format(end - start))
plt.show()
