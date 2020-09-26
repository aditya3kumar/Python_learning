class Calci():
    num = 100

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def summation(self):
        return self.num1 + self.num + self.num2




obj = Calci(2, 3)
print(obj.summation())

class Childcalci(Calci):
    num2=100


    def getdata(self):
        print('')





