""" iter() test! """
# Programmed by Shafiul Kayem!

class revrange:

    def __init__(self, var1):
        self.var1 = var1
        self.var2 = var1

    def __iter__(self):
        return self

    def __next__(self):
        if self.var1 >= 0:
            if self.var2 == self.var1:
                self.var1 = self.var1 - 1
                return self.var2
            else:
                self.var2 = self.var1
                self.var1 = self.var1 - 1
                return self.var2
        else:
            raise StopIteration

for temp in revrange(10):
    print(temp)