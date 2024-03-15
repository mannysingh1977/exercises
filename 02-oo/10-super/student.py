from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, length) -> None:
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length
    
    @property 
    def width(self):
        return  self.__width
    
    @property
    def area(self):
        return self.width * self.length
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.length)
class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    @property
    def side(self):
        return self.length
    
    # @property
    # def perimeter(self):
    #     return 4 * self.side

    # @property
    # def area(self):
    #     return self.side**2
    
class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius) -> None:
        self.__minor_radius = minor_radius
        self.__major_radius = major_radius

    @property
    def major_radius(self):
        return self.__major_radius
    
    @property
    def minor_radius(self):
        return self.__minor_radius
    
    @property
    def perimeter(self):
        raise NotImplementedError()
    
    @property
    def area(self):
        return pi * self.__minor_radius * self.__major_radius
    
class Circle(Ellipse):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius)
    
    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def radius(self):
        return self.major_radius
        