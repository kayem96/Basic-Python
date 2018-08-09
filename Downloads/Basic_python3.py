'''
This program will tells you that the number you giving is 0 or smaller or bigger? That means that (+ or -) number / positive or negative..?
'''
a = int(input('Type any intiger>>>'))
if a <= 0:
	print('{} is less than 0'.format(a))
elif a == 0:
	print('{} is equal to 0'.format(a))
else:
	print('{} is greater than 0'.format(a))
