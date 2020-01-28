import json

import pygal
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code
#将数据加载到一个列表中

filename = 'gdp_json.json'

with open(filename, 'r') as file_object:
	gdp_data = json.load(file_object)

country_gdp = {}
error_countries = []
#打印每个国家2010年的人口数量
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == 2010:
		country_name = gdp_dict['Country Name']
		gdp = float(gdp_dict['Value'])#转为浮点数在转为整数
		code = get_country_code(country_name)
		if code:
			country_gdp[code] = gdp
		else:
			error_countries.append(country_name)

print(error_countries)

with open("Error_GDP_Countries.json", 'w') as file_object:
	json.dump(error_countries, file_object)

wm_style =RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World GDP in 2010, by Country"
wm.add('GDP Map', country_gdp)

wm.render_to_file("World_GDP_LightColorized.svg")