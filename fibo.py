
""""""""""""""""""""""""""""""
# >>>>> Fibonture <<<<<
# >>>>> Shafiul Kayem <<<<<
""""""""""""""""""""""""""""""


'''''''''''''''''''''
""" fib classes! """
'''''''''''''''''''''

def abc(a):
     one = []
     x, y = 0, 1
     while y < a:
             one.append(y)
             x, y = y, x+y
     return one

if __name__ == "__main__":
	temp = abc(100)
	print(temp)