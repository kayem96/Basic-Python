print('''
This program will tells you that the number you giving is 0 or smaller or bigger? That means that (+ or -) number / positive or negative..?
''')
a = int(input('Type any intiger>>>'))
if a < 0:
	print('{} number is negative'.format(a))
else:
	print('{} number is positive'.format(a))
