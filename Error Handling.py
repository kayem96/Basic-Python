# Error Handling.
# Programmed By Shafiul Kayem.

try:
	file = open('test.py')
	view = file.read()
	print(view)
except FileNotFoundError:
	print('The file does not exist!')
finally:
	print('Hey! It is a custom error message!')