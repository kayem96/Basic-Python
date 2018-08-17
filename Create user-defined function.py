# Create a (user-defined) function.  
# Programed by Shafiul Kayem.  

def myfunction(Parameter1,Parameter2):
	if (Parameter1 < Parameter2):
		return (format(Parameter1) + ' is less than ' + format(Parameter2) + '.')

	elif (Parameter1 > Parameter2):
		return (format(Parameter1) + ' is greater than ' + format(Parameter2) + '.')

	else:
		return (format(Parameter1) + ' and ' + format(Parameter2) + ' both are same' +'.')
		
print(myfunction( 23, 24 ))
print(myfunction( 9, 9 ))
print(myfunction( 12, 4 ))