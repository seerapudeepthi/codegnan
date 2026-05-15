program to convert 24hrs clock to normal clock:
----------------------------------------------------
time = "20:37"
parts = time.split(":")
hour = int(parts[0])
min = int(parts[1])
convert = hour - 12
print(f"{time} is converted into {hour - 12}:{min} pm")

user input program :

time = input("enter 24 hours time:")
parts = time.split(":")
hour = int(parts[0])
min = int(parts[1])
convert = hour - 12
print(f"{time} is converted into {hour - 12}:{min} pm")

list:
----------
list is collection of different data types
[] and seperated by ,
list is mutable

any = [1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])

methods:
-----------    
1)append():
    
    this method is used to add new item into list,and it will in the last index positiion)
   syntax:variable_name.append(item)
any = [1,2,3]
any.append(10)
print(any)
any.append([20,30])
print(any)

immutable:
-----------
could not able to modify on that particular variable
eg:int,string
should use methods in print function to hold the particular value
any="python language"
print(any.replace("python","java"))
any.replace("python","java")
print(any)

mutable:
----------
can able to modify on that particular variable
should not use methods in print func because it directly modifies and doesn't hold values
eg:list
any = [1,2,3]
any.append(10)
print(any)
print(any.append([20,30]))

2)extend():

    this method is used to add itterable into list,and it will be in the last index position each value or substring is each index in the list
    syntax:variable_name.extend(itterables)
any=[1,2]
any.extend("python")
any.extend([10,20])
print(any)

3)pop():

    deletes the index position value
any = [1,2,3]
print(any.pop(2))--->it gives what value is deleted in output
any=[1,2,3]
any.pop(2)
print(any)----> it gives the list after removing the value

4)remove():

    used to remove item from the list ,but will mention here direct in the remove method
    syntax:variable_name.remove()
any = [1,2,3]
any.remove(2)
print(any)----->removes the element and gives the list in the output
any=[1,2,3]
print(any.remove(2))------->none

    




