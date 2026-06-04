OOPS(OBJECT ORIENTED PROGRAMMING SYSTEM):
------------------------------------------
CLASS:
    
   it is blueprint or template used to create object
   
class stu:
    name = 'deepu'
s1=stu()
print(s1.name)
__________________________________________________________________________________________
OBJECT:
    an object is an instance of a class
    
class stu:
    name = 'deepu'
s1=stu()
print(s1.name)     (here stu is class s1 is object and name is attribute)
________________________________________________________________________________________________
ATTRIBUTES:
    
    attributes are the variables that belongs to a class or an object
class stu:
    name = 'deepu'
    age = 22
s1=stu()
print(s1.name)
print(s1.age)
________________________________________________________________________________________________
METHODS:
    functions defined inside the class is methods
    
class PFS_DA:
    def python(self):
        PFS_DA = "batch_03"
        print("this pfs and da batch 003")
    def flask(self):
        PFS = "batch_03"
        print("this is pfs batch 003")
all = PFS_DA()
all.python()
all.flask()
_________________________________________________________________________________________________
CONSTRUCTOR:
    a constructor is a special method that is automatically called when object is created

class ATM:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
    def bal_check(self):
        print(f"{self.name} your total balance is :{self.balance+500}")
    def name_(self):
        print(self.name)
card = ATM(balance = 50000,name ='deepu')
card.bal_check()
card.name_()
___________________________________________________________________________________________________
ACCESS SPECIFIERS:

1.public(no underscore)
2.protected(_)
3.private(__)

PUBLIC:
--------
   *this can be accessed anywhere in the program
   *no underscore
   
class stu:
    name = 'deepu'
s1=stu()
print(s1.name)
__________________________________________________________
PROTECTED:
----------
    *this is represented using a single underscore(_)

class stu:
    _name = 'deepu'
s1=stu()
print(s1._name)
__________________________________________________________
PRIVATE:
---------
   *this is represented using a double underscore(__)
   *syntax:print(object._ classname __ attribute)

class stu:
    __name = 'deepu'
s1=stu()
print(s1._stu__name)
____________________________________________________________

ENCAPSULATION:
    it is the process of binding data and methods together

class bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo(self,amount):
        self.__balance += amount
    def get_bal(self):
        return self.__balance
acc = bank(1000)
acc.depo(10000)
print(acc.get_bal())
print(acc._bank__balance)































    
