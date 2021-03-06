from car import Car

class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery_size = 70
		self.battery = Battery()
	
	def describe_battery(self):
		print("{0} has a {1} {2}.".format(self.get_descriptive_name(), str(self.battery_size), "-kWh battery"))
	
	def fill_gas_tank(self):
		print("Electric Car has no gas_tank.")

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	
	def __init__(self, battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range) + " miles on a full charge"
		print(message)
	
	def update_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85