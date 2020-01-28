filename = 'guest.txt'
with open(filename, 'w') as file_object:
	guest_name = input("Input your name:")
	file_object.write(guest_name.title() + '\n')

with open(filename, 'a') as file_object:
	while True:
		guest_name = input("Input your name:")
		print('Hello {}'.format(guest_name.title()))
		file_object.write(guest_name.title() + '\n')
		if input("Continue (yes/no)?:") == 'no':
			break

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())