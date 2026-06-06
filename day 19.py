POLYMORPHISM:
--------------
having many forms .it allows the same function,method or operator,to behave differently depending on object

1.method overloading:
----------------------
   defining multiple methods with same name but different parameters

class calculator:
    def add(self,a,b,c=0):
        return a + b + c
an = calculator()
print(an.add(23,6,24))

          or
          
class calculator:
    def add(self,a,b):
        return a + b
    def add(self,a,b,c=3):
        return a + b+ c
an = calculator()
print(an.add(23,6))
print(an.add(23,8,2))

_______________________________________________________________________________________________________________________________________________________________
2.method overriding:
---------------------
    this occurs when a child class provides its own implementation of a method already defined in the parent class
    
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
ntg = dog()
ntg.sound()
________________________________________________________________________________________________________________________________________________________________--

3.operator overloading:
-----------------------
      this allows operators such as +,-,* etc ,, to perform different actions for user - defined objects
class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,b):
        return self.marks / b.marks
any = stu(78)
so = stu(4)
print(any + so)

note:the operator inside the method will overload a special method or operator given in the call

_______________________________________________________________________________________________________________________________________________________________________________
ABSTRACTION:
-------------
   -> this is the process of hiding internal implementation details and showing only essential features to user
   ->it focuses on what an object does rather than how it does it....
    
from abc import ABC,abstractmethod
class shape(ABC):
    
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeters(self):
        return 2*(self.a + self.b)
an = Rec(10,5)
print(an.area())
print(an.perimeters())


































