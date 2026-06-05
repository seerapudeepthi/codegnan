INHERITANCE:

    this allows one class to aquire the properties and methods from another class

types:
1.single inheritance
2.multi inheritance
3.multilevel inheritance
4.hierarchial inheritance
5.hybrid inheritance

single inheritance:
--------------------
a child class inherits from a single parent class

class father:
    def Land(self):
        print("my father has 5 acres")

class Deepu(father):
    def my_own(self):
        print("i have 2 acres")

fam = Deepu()
fam.Land()

multiple inheritance:
---------------------
child class inherit from more than one class

class father:
    def Land(self):
        print("my father has 5 acres")
class mother:
    def gold(self):
        print("mother has 1kg gold")

class deepu(father,mother):
    def mine(self):
        print("i have nothing")

fam = deepu()
fam.Land()
fam.gold()

multi-level inheritance:
--------------------------
      a child class inherits from a parent class and another class inherits from that child class
class grandfather:
    def land(self):
        print("grand father has 5acres of land")
class father(grandfather):
    def flat(self):
        print("father has flat at BNG")
class child(father):
    def mine(self):
        print("i have nothing")
assets = child()
assets.land()
assets.flat()

hierarchial inheritance:
-------------------------
    multiple child classes inherits from a single parent class

class father:
    def Land(self):
        print("father has 5 acres")
class brother(father):
    def Asserts(self):
        print("job")
class sister(father):
    def Assert(self):
        print("jobless")
a = brother()
b = sister()
a.Land()
b.Land()


hybrid inheritance:
-------------------
combination of two or more inheritances

class A:
    def some(self):
        print("class A")

class B(A):
    def any(self):
        print("class B")
class C(A):
    def so(self):
        print("class C")
class D(B,C):
    def all(self):
        print("class D")
hye = D()
hye.some()
hye.any()
hye.so()
hye.all()

super() method:
---------------
super() is used to access methods and constructor of parent class from child class

class parent:
    def dis(self):
        print("method parent")
class child(parent):
    def display(self):
        super().dis()
        print("method child")
any = child()
any.display()


class Person:
    def __init__(self,name):
        self.name = name
class stu(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll 
    def show(self):
        print(f"Name:{self.name}")
        print(f"Roll:{self.roll}")
any = stu("deepu",105)
any.show()

















































    
