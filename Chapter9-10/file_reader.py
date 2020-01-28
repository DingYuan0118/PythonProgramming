import os.path

base_path = os.path.dirname(os.path.realpath(__file__))  #获取当前路径

# 打印当前目录(当前目录不一定为文件所在目录)
print(os.getcwd())

with open(os.path.join(base_path,'pi_digits.txt')) as file_object:
	contents = file_object.read()
	print(contents, end = '')
print() #插入空行

with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
		
with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

