import unittest
from city_function import get_formmatted_cityname

class CityNameTestCase(unittest.TestCase):
	"""测试城市名"""
	def test_city_name(self):
		formmatted_name = get_formmatted_cityname("santiago", 'Chile')
		self.assertEqual(formmatted_name, 'Santiago Chile')
	
	def test_city_country_population(self):
		formmatted_name = get_formmatted_cityname("santiago", 'Chile' , 'population=50000')
		self.assertEqual(formmatted_name, 'Santiago, Chile - Population 50000')
unittest.main()