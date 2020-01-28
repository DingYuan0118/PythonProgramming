import csv
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取最高气温
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'
def plot_temperaturemap(filename):
	with open(filename, 'r') as file_object:
		reader = csv.reader(file_object)
		header_row = next(reader)
	
		dates ,highs, lows = [], [], []
		
		for row in reader:
			try:	
				current_date = datetime.strptime(row[0], "%Y-%m-%d")
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(current_date, "missing data")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)
				#print(highs)
	
	#根据数据绘制图形
	fig = plt.figure(dpi=128, figsize=(10, 6))
	plt.plot(dates, highs, c='red', alpha=0.5)
	plt.plot(dates, lows, c='blue', alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
	
	#设置图形的格式
	plt.title("Daily high and low temperatures - 2014\nDeath Vally, CA", fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	
plot_temperaturemap(filename_1)
plot_temperaturemap(filename_2)
plt.show()