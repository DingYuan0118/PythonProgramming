import json

#将数据加载到一个列表中
filename = 'population_data.json'

with open(filename, 'r') as file_object:
	pop_data = json.load(file_object)
	
#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = pop_dict['Value']
		print(country_name + ": " + population)