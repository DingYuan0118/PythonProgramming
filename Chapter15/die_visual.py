import pygal
import matplotlib.pyplot as plt

from die import Die

#创建一个D6(6面骰子)
die_1 = Die()
die_2 = Die(10)
#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#print(results)	
#分析结果
frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 and one D10 50000 times."
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = 'Result'	
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

plt.figure(figsize=(10,6))
plt.plot(hist.x_labels, frequencies, linewidth=5)
plt.scatter(hist.x_labels, frequencies, s=5)

plt.xlabel("Result", fontsize=10)
plt.ylabel("Frequency of Result", fontsize=10)
plt.title("Results of rolling one D6 and one D10 50000 times.")
plt.show()
