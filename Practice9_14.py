from random import randint

class Dice():
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll_dice(self):
		x = randint(1,self.sides)
		print(x, end = '')
		
my_dice = Dice()
my_dice2 = Dice(10)
my_dice3 = Dice(20)
# print自带换行符
for i in range(10):
	my_dice.roll_dice()
print()
for i in range(10):
	my_dice2.roll_dice()
print()
for i in range(10):
	my_dice3.roll_dice()


