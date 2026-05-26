BUILT IN FUNCTIONS:
-------------------------------------------------------------------------------------------------------
print():
n=5
print(n)
-------------------------
input():
n = int(input())
print(n)
---------------------------
type():
n = 5
print(type(n))
------------------------------
len():
    a =[1,2,4]
    print(len(a))
-----------------------------   
max():
    a=[2,4,5]
    print(max(a))
-------------------------------
min():
    a =[2,4,5]
    print(min(a))
-----------------------------
m = [3,4,1,2]
m.sort()
print(m)
------------------------------
m = [3,4,1,2]
m.sorted()
print(m)
----------------------------------------------------------------------------------------------------------

RECURSIVE FUNCTIONS:

 a recursive function that calls itself to solve a problem by breaking it into small or simple sub -problems

def fac(num):
    if num == 1:
        return 1
    return num *fac(num-1)
print(fac(5))
-------------------------------------------------------------------------------------------------------------

RETURN():

    this ends a function execution and sends a value back to code that called the function
    
def add(a,b):
    return a + b
res = add(4,5)
print(res)
-------------------------------------------------------------------------------------------------------------
LAMBDA FUNCTION:

a lambda function is a small anonamous functions
it will take n no of arguments but only one expression
syntax:lambda arguments:expression

so = lambda a,b,c:a+b+c+a
print(so(3,4,9))

so = lambda a,b:a-b
print(so(4,5))























    
