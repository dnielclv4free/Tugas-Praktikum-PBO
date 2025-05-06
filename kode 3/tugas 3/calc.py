import math 

class Opr:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        if isinstance(other, Opr):
            return Opr(self.x+other.x)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, Opr):
            return Opr(self.x-other.x)
        else:
            pass
    def __mul__(self, other):
        if isinstance(other, Opr):
            return Opr(self.x*other.x)
        else:
            pass
    def __truediv__(self, other):
        if isinstance(other, Opr):
            return Opr(self.x/other.x)
        else:
            pass
    def __pow__(self, other):
        if isinstance(other, Opr):
            return Opr(self.x**other.x)
        else:
            pass

    def __log__(self, other):
        # Menggunakan math.log untuk menghitung logaritma dengan basis tertentu
        if self.x <= 0:
            return "Error: Logarithm undefined for non-positive values"
        return math.log(self.x, other.x)

    def __str__(self):
        return f"({self.x})"


point1 = Opr(100)
point2 = Opr(10) #digunakan sebagai base untuk logaritma juga

print(f"Penjumlahan : {point1 + point2}")
print(f"Pengurangan : {point1 - point2}")
print(f"Perkalian : {point1 * point2}")
print(f"Pemabagian : {point1 / point2}")
print(f"Perpangkatan : {point1 ** point2}")
print(f"Logaritma : {point1.__log__(point2)}")
