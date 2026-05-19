type conversions:
------------------
int :
------
int can be converted into string and float
an = 78
us = str(an)
om = float(an)
some = list(an)
print(om)
print(type(us))---><class str>
print(type(om))----><class float>
print(type(some))----->TypeError
----------------------------------------------------------------------
string:
----------
string can be converted into int,list
an = "python"
some = int(an)
print(some)#---->ValueError

an = "78"
some = int(an)
print(some)---->78

an = "90"
some = list(an)
print(some)---->['9','0']

-----------------------------------------------------------
float:
----------    
    float can be converted into int,string
an = 78.22
some = int(an)
print(some)--->78

car = 90.78
print(int(car))
print(type(str(car)))----><class str>
-----------------------------------------------------------------
list:
-------------    
    list can be convert into tuple and string 
an = [1,10]
some = str(an)
print(type(some))#---><class str>
print(tuple(some))#--->('[', '1', ',', ' ', '1', '0', ']')
-------------------------------------------------------------------
tuple:
-----------
   tuple converted to list
an = (1,2)
some = list(an)
print(some)#----->[1,2]
--------------------------------------------------------------------
--------------------------------------------------------------------


int as user input:
---------------------------------
n = int(input("enter a number:"))
print(89+n)#--->enter a number:45
           #135

str as user input:
----------------------------
some = input("write a text:")
print(some)#---->write a text:hi good morning
                #hi good morning
list as user input:
----------------------------
any = input("enter number:").split()
print(any)#---->enter number:3 45 6
               #['3', '45', '6']

any = list(map(int,input("enter numbers:").split()))
print(any)#---->enter numbers:3 45 6
                #[3, 45, 6]


tuple as user input:
------------------------------
an = tuple(map(int,input("enter the values:").split()))
print(an)#----->enter the values:3 4 5
               #(3, 4, 5)

an = eval(input("enter:"))
print(an)#----->enter:"78"
         #78










