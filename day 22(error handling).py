ERROR HANDLING:
________________________
    
1.TRY BLOCK:

    it will test a block of code for error

2.EXCEPT:

    the except block let handle if the code contains error

3.ELSE BLOCK:

    this will be executed,if try block has no error in the code
    
4.FINALLY:

     this will be executed either try block contain error or not


try:
    print(10/0)
except:
    print("this will handle ZeroDivisionError")

_______________________________________________________________________________________   
a = 12
b = "hi"
try:
    print(a + b)
except:
    print("this is syntaxerror")
_____________________________________________________________________________________________
a = 10
try:
    print(len(a))
except:
    print("this is a attribute error")
______________________________________________________________________________________________
a ="hi this is python"
try:
    print(len(a))
except:
    print("this is syntaxerror")
______________________________________________________________________________________________
a = 10
try:
    print(b)
except:
    print("this is name error")
______________________________________________________________________________________________

try:
    print("hi"+" " + "py")
except NameError:
    print("this will handle NameError")
else:
    print("no error")
_______________________________________________________________________________________________
try:
    print(29+ "py")
except NameError:
    print("this will handle NameError")
else:
    print("no error")
_________________________________________________________________________________________________
try:
    print(5+"py")
    print(a)
except TypeError:
    print("this will handle TypeError")
except NameError:
    print("this will handle NameError")
else:
    print("no error")

note : it prints only the first error in try block and exit the block
_______________________________________________________________________________________________
try:
    print(a)
except:
    print("Error")
else:
    print("no error")
finally:
    print("true")













    
