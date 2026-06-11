FILE HANDLING:
__________________________________________________________

file handler is an object of file to maintain several functions of file like creating,reading,updating,and deleting the file

opening a file:
________________

1.open()
2.with open()

syntax: name = open('filename','mode')
       -------
       -------
       close()
       
so = open('DSA DAY1(introduction)'.txt','r')
print(so.read)
so.close()
____________________________________________________________________________________________________________
modes:

'r'-> is used to reading the file,error if file does not exist...
'a'-> is used to add the text into file if file does not exist it will throw the error......
'w'-> is used to add the txt into file but it will override of all txt inside file...if the file doesn't exist it will create with that name...
'x'->is used to create the file....but will throw error if we are used 'r' mode to create....

_______________________________________________________________________________________________________________
______________________________________________________________________________________________________________
METHODS:

1)write():
    
so = open('demo.txt','w')
print(so.write("this is python"))
so.close()

with open('demo.txt','w') as so:
    so.write("java")
with open('demo.txt','w') as so:
    print(so.write("java"))
_____________________________________________________________________________________________________________
2)read():
    this method can read entire file chunk by chunk where we can specify the

any = open('demo.txt','r')
print(any.read())
any.close()

with open('demo.txt','r') as any:
    print(any.read())

with open('demo.txt','r') as any:
    print(any.read(2))
----------------------------------------------------------------
3)readline(): can read only one line at a time in a file...
    
with open('demo.txt','r') as any:
    print(any.readline())
--------------------------------------------------------------
4)readlines():it will read entire file and gives in a list where each line is each index in a list
     
with open('demo.txt','r') as any:
    print(any.readlines())
____________________________________________________________________________________________________
5)delete():
    to delete a file
import os
os.remove('demo.txt')




















