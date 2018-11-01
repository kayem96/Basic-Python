#Factorial Practice
#Programmed by Shafiul Kayem

num = int(input("Enter your number: "))
tmp = num

while num > 1:
	num -= 1
	tmp *= num
if tmp == 0:
	print(1)
else:
	print(tmp)