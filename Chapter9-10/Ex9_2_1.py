import logging
#logging.basicConfig(level=logging.INFO)

class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
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
		
my_new_car = Car("audi", "a4", 2016)
logging.info(my_new_car.make)
logging.info(my_new_car.model)
logging.info(my_new_car.year)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car_2 = Car("BMW", "S3", 2015)
my_new_car_2.update_odometer(12)
my_new_car_2.read_odometer()
my_new_car_2.update_odometer(11)
my_new_car_2.read_odometer()
my_new_car_2.increment_odometer(12)
my_new_car_2.read_odometer()

