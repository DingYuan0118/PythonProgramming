import json

#存在多个函数调用，定义全局filename
filename = 'username.json' 

def get_stored_username():
	'''如果存储了用户名，就获取它'''
	#filename = 'username2.json'
	try:
		with open(filename, 'r') as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username
		
def greet_user():
	'''问候用户并指出其名字'''
	username = get_stored_username()
	sign = input("Is '{}' your name?(yes/no) ".format(username))
	while True:
		if sign == 'yes':
			print("Welcome back, " + username + "!")
			#打断循环
			break 
		elif sign == 'no':
			username = get_new_username().title()
			with open(filename, 'w') as file_object:
				json.dump(username, file_object)
				print("We'll remember you when you come back, " + username + "!")
			#打断循环
			break
		else:
			print("Please enter 'yes' or 'no'！")
			sign = input("Is '{}' your name?(yes/no) ".format(username))
	return username

def get_new_username():
	username = input("What is your name? ")
	with open(filename, 'w') as file_object:
		json.dump(username, file_object)
	return username

greet_user()
	

