import unittest
from Practice11_3 import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		'''初始化'''
		self.employee = Employee('Ding', 'Yuan', 3000)
		
	def test_give_default_raise(self):
		'''测试默认的加薪'''
		base = self.employee.salari
		self.employee.give_raise()
		self.assertEqual(base + 5000, self.employee.salari)
	
	def test_give_custom_raise(self, salari = 800):
		'''测试自定义的加薪'''
		base = self.employee.salari
		self.employee.give_raise(salari)
		self.assertEqual(base + salari, self.employee.salari)
		
unittest.main()