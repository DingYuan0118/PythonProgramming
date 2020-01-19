'''class Dog():
	"""一次模拟小狗的简单尝试"""
	
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
	
	def sit(self):
		print(self.name.title() + "is now sitting.")
		
	def roll_over(self):
		print(self.name.title() + "rolled over!")
		
my_dog = Dog("willie", 6)
print("My dog`s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()'''
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
	

restaurant_1 = Restaurant('1', '2')
restaurant_1.print_restaurant_stat() 
restaurant_1.open_restaurant()
restaurant_2 = Restaurant("Ding", "Chinese Food")
restaurant_2.set_number_served(11)
restaurant_2.increment_number_served(11)