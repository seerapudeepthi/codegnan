NESTED LOOP:
-----------
for i in range(1,2):
    for j in range(1,2):
        print(i)
        print(j)
----------------------------------------------------
1)PRORGRAM FOR TABLES:

num = 9
for i in range(1,11):
    print(f"{num}*{i}={i*num}")
----------------------------------------------------
2)PROGRAM FOR PALINDROME:

so = input("enter string:")
temp = ""
for j in so:
    temp = j + temp
print(temp)
if temp == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not palindrome")
----------------------------------------------------------
3)PROGRAM FOR ARMSTRONG:
     
num = 153
temp = 0
len = len(str(num))
for i in str(num):
    temp += int(i)**len
if temp == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not armtsrong number")
-------------------------------------------------------------
4)PROGRAM FOR PERFECT NUMBER:
    
num = 28
perfect = 0
for j in range(1,num):
    if num%j==0:
        perfect += j
if perfect == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")
--------------------------------------------------------------
5)PROGRAM FOR PRIME NUMBER:

num = 5
count = 0 
for i in range(1,num+1):
    if num%i== 0:
        count += 1
if count == 2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
---------------------------------------------------------------

PATTERNS:

star = 5
for i in range(1,star+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
                                         

star = 5                              
for i in range(1,star+1):
    for j in range(1,i+1):                      
        print(chr(64+j),end=" ")
    print()
--------------------------------------------------------------------
star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(count,end=" ")
    print()
---------------------------------------------------------------------
star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(j,end=" ")
    print()
-------------------------------------------------------------------------
star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(i,end=" ")
    print()
-------------------------------------------------------------------------
star = 5
count = 0
for i in range(star,0,-1):
    for j in range(i):
        count += 1
        print("*",end=" ")
    print()
--------------------------------------------------------------------------
n = 5
for i in range(1,n+1):
    print(" "*(n - i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()











              
