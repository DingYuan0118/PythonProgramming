import logging
logging.basicConfig(level=logging.INFO)

class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		self.gas_tank = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + " " + self.model
		return long_name.title()
		
	def read_odometer(self):
		print(self.get_descriptive_name()+ " has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		"""
		mileage---英里数
		将里程表读数设置为指定的值
		禁止将里程表读数往回调
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")
	
	def increment_odometer(self, miles):
		"""increment---增量"""
		self.odometer_reading += miles
	
	def fill_gas_tank(self):
		self.gas_tank = 20
		
		
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
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
#logging.info(my_tesla.gas_tank)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()