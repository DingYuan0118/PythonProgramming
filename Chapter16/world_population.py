import json

import pygal
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

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

#根据人口数量将所有国家分为三组
country_pops_1, country_pops_2, country_pops_3 = {}, {} ,{}
for country, population in country_population.items():
	if population < 1e7:
		country_pops_1[country] = population
	elif population < 1e9:
		country_pops_2[country] = population
	else:
		country_pops_3[country] = population

#看看每组分别包含多少个国家
print(len(country_pops_1), len(country_pops_2), len(country_pops_3))


wm_style =RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', country_pops_1)
wm.add('10-100m', country_pops_2)
wm.add('>1bn', country_pops_3)

wm.render_to_file("World_population_LightColorized.svg")