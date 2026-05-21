'''ELIF:
-----
  used to check more conditions
  
stu_marks = int(input("enter marks:"))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("pass")
else:
    print("fail")
    

1)program to find maximum number from three numbers:
---------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(f"{a} is greater")
elif b > a and b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
---------------------------------------------------------------------------------------------------------

NESTED IF :
----------
declaring if statement in if statement
    
1)program for SBI ATM :
-------------------------
SBI_bank = {"ATM PIN":"6600"}
pin = input("enter 4 digit ATM pin:")
if len((pin)) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("welcome to SBI ATM")
    else:
        print("Invalid pin")
else:
    print("pls enter 4 digit pin")

---------------------------------------------------------------------------------------------------------
FOR LOOP:
----------
 *used to itterate over a sequence
 *the variable we use in for loop is initial variable or instance variable

any = "python"
an =[1,2,3,4]
so = (5,6,7,8)
for how in any:
    print(how,end=" ")

RANGE():
---------
*range is a inbuilt function used to generate numbers in sequencial manner
*syntax : range(start,end,step)
for i in range(1,5):
    print(i,end =" ")#---->1 2 3 4
    
ELSE IN FOR LOOP:
-------------------
for i in range(1,10):
    print(i,end=" ")
else:
    print("code ended here")
    
-----------------------------------------------------------------------------------------------------------------
CONTROL STATEMENTS:
-------------------
1)BREAK():
--------
 used to exit from the loop based on condition

for i in range(1,10):
    if i == 5:
        break
    print(i)

2)CONTINUE():
-------------
used to skip the current iteration based on the condition

for i in range(1,10):
    if i == 5:
        continue
    print(i,end=" ")

3)PASS():
---------
pass is a space holder

for i in range(1,10):
    if i == 3:
        pass
    print(i,end=" ")
-----------------------------------------------------------------------------------------------------------------
WHILE LOOP:
------------'''

i = 1
while i < 5:
    print(i)
    i += 1





















    
