'''提供Restaurant类'''
class Restaurant():
	def __init__(self, name, type):
		self.restaurant_name = name
		self.cuisine_type = type
		self.stat = False
		self.number_served = 0
	
	def describe_restaurant(self):
		print("This restaurant's name is " + self.restaurant_name.title())
		print("This restaurant's cuisine type is " + self.cuisine_type.title())
		
	def print_restaurant_stat(self):
		print("Restaurant is open.") if self.stat == True else print("Restaurant is closed.")
		
	def open_restaurant(self):
		if self.stat == False:
			self.stat = True
		else:
			self.stat = True
		self.print_restaurant_stat()
	
	def set_number_served(self, numbers):
		self.number_served = numbers
		print("Now served {} customers.".format(self.number_served))
	
	def increment_number_served(self, numbers):
		self.number_served += numbers
		print("Now served {} customers.".format(self.number_served))
	