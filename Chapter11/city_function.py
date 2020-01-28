def get_formmatted_cityname(city , country, population=''):
	"""得到格式化城市名"""
	if population:
		formmatted_name = "{0}, {1} - {2}".format(city, country, population.replace("=", ' '))
	else:
		formmatted_name = "{0} {1}".format(city, country)
	return formmatted_name.title()