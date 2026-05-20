F-STRING or DOC STRING:
-----------------------
num = 10
if num%2 == 0:
    print(f"{name}is a even number")--->10 is even number 
---------------------------------------------------------------------------------------------------------------------------------
STATEMENTS:
----------  
    statements are of three types
      1)condition statements--->(if,elif,if-else)
      2)control flow statements---->(break,continue,pass)
      3)loop statements--->(for,while)

condition statements:
--------------------
1) if : to check statement is true or not

num = 6
if num%2==0:
    print("even")--->even
--------------------------------------------------------------------------------------------------------------------------------------------------------
2)if-else : else in the if statement incase the condiiton becomes false
            then it will enter into fall back(else),it will whatever inside it
            
program to print whether number is even or odd:
------------------------------------------------    
num = 7
if(num%2==0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
    
program to check for voting:
-------------------------------------------------
age = int(input("enter your age:")
if age>=18:
    print("eligible to vote")
else:
    print(f"you have to wait for (18-age}more years")

program for greater number:
------------------------------------------------
num = 8
num2 = 15
if num>= num2:
    print(f"{num} is greater number than {num2}")
else:
    print(f"{num2}is greater number than {num}")


program for leap year:
-----------------------------------------------
year = int(input())
if (year%4==0 and year%100!=0) or year%400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

program to print whether vowel or consonants:
----------------------------------------------
vowel ="a"
if vowel in "AEIOUaeiou":
    print(f"{vowel} is a consonants")
else:
    print(f"{vowel} is a consonants")


program for negative or positive numbers:
-----------------------------------------
num = -9
if num>=0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")

program for pass or fail:
---------------------------------------
marks = int(input("enter your marks:"))
name = input()
if marks>=45:
    print(f"{name} is pass")
else:
    print(f"{name} is fail")

program for divisiblitiy:
-----------------------------------------
num = 75
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

program for traffic signal:
---------------------------
signal = int(input("enter \n1.red \n2.green:"))
if signal == 1:
    print("pls stop")
else:
    print("go")































    
          
