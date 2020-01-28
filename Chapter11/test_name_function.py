import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#继承unittest
	"""测试name_function.py"""
	
	def test_first_last_name(self):#自动识别test_开头
		"""能够正确地处理向Janis Joplin这样的姓名吗"""
		formatted_name = get_formatted_name('janis', 'Joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')#断言判定
	
	def test_first_last_middle_name(self):#自动识别test_开头
			"""能够正确地处理向Janis Joplin这样的姓名吗"""
			formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
			self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')#断言判定
		
unittest.main()#调用unittest