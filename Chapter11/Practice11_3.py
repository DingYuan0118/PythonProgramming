class Employee():
	def __init__(self, first_name, last_name, salari):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.salari = salari
		
	def give_raise(self, salari_plus = 5000):
		self.salari += salari_plus