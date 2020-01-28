import os

filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	'''current_path = os.getcwd()
	msg = "Sorry, the file {} does not exist.".format(current_path + "\\" + filename)
	print(msg)'''
	pass
else:
	#计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file" + filename + " has about " + str(num_words) + " words.")
	print(contents.lower().count('the'))