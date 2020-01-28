def add(num1, num2):
	try:
		sum = int(num1) + int(num2)
	except :
		print("You can only input numbers!")
	else:
		print("The sum is : {}".format(sum))
num1 = input("Please input the first numbers: ")
num2 = input("Please input the second numbers: ")
add(num1, num2)

while True:
	sign = input("Enter 'q' to quit:")
	if sign == 'q':
		break
	num1 = input("Please input the first numbers: ")
	num2 = input("Please input the second numbers: ")
	add(num1, num2)