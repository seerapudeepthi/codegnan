a = 3
b = 5
print(a//b)

operators
-----------
i)arithmetic operator :
-----------------------   

    +,-,*,%,/,//,**

a = 2
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)


ii)assignment operators:
------------------------   

    = ,+= ,-= ,%= ,*=
    
count = 0
for j in range(0,11):
    count+=1
print(count)



iii)comparision operator:
-------------------------    

       == , <= ,>= ,> , < , !=

a = 4
b = 5
print(a==b)


iv)identity operator:
---------------------
is -> this operator looks for object location is same or not
== -> this operator looks for same value

a = [1,2]
b = [1,2]
c = a
print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(type(a))
print(a is not b)

v)logical operators:
-----------------------
and , or , not

and -> this is used to check both should be true/if both conditions are true then only it is true

a = 15
if a%3==0 and a%5==0:
    print("True")
    
or -> if any one condition is true then it is true

a = 15
if a%3==0 or a%5==0:
    print("True")

vi)membership operators:
------------------------
     in,not in
a = 3
b = [1,2,3]
c = 5
print(a in b)
print(c not in b)

vii)bitwise operators:
-----------------------
 &,|,<<,>>
print(5 & 3)
print(5 | 3)
print(5 << 3)
print(5 >> 3)

string:
--------------------------
string is sequence of characters that are enclosed in '' , "" , (''' '''(comments)),immutable
name = " python5& "
for i in name:
    print(i)

methods:
    
1)replace():

    syntax : variable_name.replace("old string","new string")
    
any = " python is a language"
print(any.replace("python","java"))
print(any)

2)split():

  seperate into parts and it will split based on the substring where before substring is one index and after is another index in the list form 
any = "python is a language"
print(any.split())

3)len():

    gives the length of the string
    syntax:len(variable_name)
any = "python is a language"
print(len(any))

4)slicing():

    slicing can guive the access to get particular index of a string
    syntax:variable_name[start : ending]

any = "python is a language"
print(any[3:11])

5)indexing():
    
     used to get the substring present in that index position
    syntax:variable_name[index positon]
    
any = "python is a language"
print(any[7])
print(any.index("ang"))
    
   
    




     
    
    

    
    
