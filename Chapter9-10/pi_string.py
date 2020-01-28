with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
pi_string = ''

for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

num = '926'
if '926' in pi_string:
	print("True")