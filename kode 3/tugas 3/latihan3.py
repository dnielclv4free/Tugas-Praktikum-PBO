from abc import ABC, abstractmethod

class Shape:
    def __init__(self, name):
        self._name=name
        
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def name(self):
        return self._name

class Circle(Shape):
    def __init__(self,name, radius):
        super().__init__(name)        
        self._radius = radius


    def area(self):
        return 3.14 * (self._radius ** 2)

    def __str__(self):
        return f"{self.name} with radius {self._radius}"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        
        return raise TypeError("Unsupported")

class Square(Shape):
    def __init__(self,name, side):
        super().__init__(name)        
        self._side = side


    def area(self):
        return self._side ** 2

    def __str__(self):
        return f"{self.name} with side {self._side}"
    
    def __add__(self, other):
        if isinstance(other, Square):
            return Circle(self._side + other._side)
        else : 
            return raise TypeError("Unsupported")

def print_shape_info(shape):
    print(f"{shape.name} has an area of {shape.area()}")

circle1= Circle(lingkaran1, 5)
circle2 = Circle(lingkaran2, 3)
square1 = Square(persegi1, 4)
square2 = Square(persegi2, 6)

print_shape_info(circle1)
print_shape_info(square2)

circle3 = circle1+circle2

print_shape_info(circle3)

def print_area(shape):
    try:
        print(f"The area is : {shape.area()}")
    except AttributeError :
        print("Objek tidak ada area mtehod")

print_area(circle1)
