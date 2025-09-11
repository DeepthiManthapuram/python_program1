from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def area(self, length, breadth):
        return length * breadth
    
class Circle:
    def area(self, radius):
        return 3.14 * radius * radius