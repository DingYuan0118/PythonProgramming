with open("learning_python.txt") as file_object:
	contents = file_object.read()
	print(contents, end = '')
print()
with open("learning_python.txt") as file_object:
	for line in file_object:
		print(line.rstrip().replace('python', 'c'))

with open("learning_python.txt") as file_object:
	for line in file_object.readlines():
		print(line.rstrip().replace('Python', 'c'))