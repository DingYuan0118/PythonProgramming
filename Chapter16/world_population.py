import json
import pygal
from pygal.maps.world import World

from country_codes import get_country_code
#将数据加载到一个列表中

filename = 'population_data.json'

with open(filename, 'r') as file_object:
	pop_data = json.load(file_object)

country_population = {}
#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))#转为浮点数在转为整数
		code = get_country_code(country_name)
		if code:
			country_population[code] = population
			
wm = World()
wm.title = "World Population in 2010, by Country"
wm.add('2010', country_population)

wm.render_to_file("World_population.svg")