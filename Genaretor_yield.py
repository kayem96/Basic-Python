""" Genaretor Practice! Making Sequence using yield """
""" programmed by Shafiul Kayem """

def revrange(var1):
	while var1 >= 0:
		yield var1
		var1 -= 1

for println in revrange(10):
	print (println)
