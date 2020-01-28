import json

filename = 'username.json'
with open(filename, 'r') as file_object:
	try:
		username = json.load(file_object)
	except:
		pass
	else: 
		print("Welcome back, " + username + "!")