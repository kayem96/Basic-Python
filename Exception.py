#  Exception Handling.
# Programmed By Shafiul Kayem!
try:
	print('Please Enter any number for divide!')
	tmp = int(input('First Number : '))
	temp = int(input('Second Number : '))
	print (tmp, '/', temp, '=', tmp/temp)
except ZeroDivisionError:
	print (tmp, '/', temp, '=', tmp)
