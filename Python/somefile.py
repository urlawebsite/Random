class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def reduce(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            a, b = b, a % b
        self.numerator = self.numerator // a
        self.denominator = self.denominator // a

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


x = fraction(2*3*4, 4*3*5)
y = fraction(2*7, 7*2)
z = fraction(13, 14)
a = fraction(13*2*7, 14)
print(x)
print(y)
print(z)
print(a)
