'''ASSERT ERROR:
--------------
this is debugging statement used to test whether a condition is true
we don't use semicolon at the end

num =10
assert num > 5
print("True")

age = 19
assert age > 10
print("Eligible")

FUNCTIONS:
----------
1)function is block of code which only execute when it is called
2)the values we define in def statement are parameters
3)the values we pass while calling function is arguments
4)to avoid repeated lines in code
5)function is defined using def keyword

def function_name(parameters):-----definition line
    ------------------
    ------------------
function_name(arguments)--------->calling function

1)num = 9
def even(num):
    print(num)
even(num)
--------------------------------------------    
2)num = 8
def even(num):
    if num %2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num)
even(109)
---------------------------------------------
WAYS TO PASS ARGUMNETS:

1)required arguments:

     function must be called with the same number of arguments as parameters

def even(num,num1,num2):
    if num1   %2==0:
        print("even")
    else:
        print("odd")
even(5,10,15)
-----------------------------------------------------------------------------------------
2)default arguments:

 by default values are defined at parameters even though it will take from arguments 

def details(name = "deepu"):
    print(name)
details("deepthi")
details("deepu")
--------------------------------------------------------------------------------------------
3)keyword arguments:

  we can send arguments with key=value syntax .by this,the order of arguments does not matter

def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even(name = "deepu",age = 22,sal = 75000)
------------------------------------------------------------------------------------------------
4)variable length arguments:

    adding a star(*)before the parameter name function,receive a tuple of arguments and can access items with indexes
          
def even(*name):
    print(name[2])
even("deepu","mohana","dinesh","srinu")
-------------------------------------------------------------------------------------------------
5)reference arguments:
       
name = "deepu"
def even(any):
   print(any)
even(name)
---------------------------------------------------------------------

1)PROGRAM FOR TABLES:

def tables(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
tables(9)

2)PROGRAM FOR PALINDROME:

def palindrome(string):
    temp=""
    for j in string:
        temp = j + temp
    if temp == string:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not palindrome")
palindrome("madam")
palindrome("python")

3)PROGRAM FOR ARMSTRONG:'''

def armstrong(num):
    temp= 0
    length = len(str(num))
    for i in str(num):
        temp += int(i)**length
    if temp == num:
        print(f"{num} is a armstrong number")
    else:
        print(f"{num} is not armstrong number")
armstrong(153)
    















