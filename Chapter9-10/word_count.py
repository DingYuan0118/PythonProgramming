import os

def count_words(filename):
	'''计算一个文件大致包含多少单词'''
	try:
		with open(filename, 'r', encoding='UTF-8') as file_object:
			cotents = file_object.read()
	except FileNotFoundError:
		'''current_path = os.getcwd()
		msg = "Sorry, the file {} does not exist.".format(current_path + "\\" + filename)
		print(msg)'''
		pass
	else:
		#计算文件大致包含多少个单词
		words = cotents.split()
		num_words = len(words)
		print("The file" + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'mobi_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

