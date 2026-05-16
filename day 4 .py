concatenation :
----------------------
for integers it will to addition
for strings it will combine sentences
a= 90
b = 8
print(a+b)
any= "python"
so = " is a language"
on = 7
print( any +so)----> python is a language
print( any + so +on)------>int will not add with strings
an = [1,2]                                                                                   string,tuple -> immutable
am = [3,4]                                                                                    list -> mutable
print(an +am)----->[1,2,3,4]

tuple:
----------
collection of different data types separated by commas,represented in ()
tuple is immutable
some =(1,"python",[1,2],(3,4))
print(some)------>(1,"python",[1,2],(3,4))
print(some[2][1])----->2

methods:

i)count():

    this is used to count the particular item in the tuple
    syntax:variable_name.count(item)
some = (1,"python",[1,2],(3,4),"python")
print(some.count("python"))----->2

ii)index():

    used to find index position of the item and only gives the first occurence
    
some = (1,"python",[1,2],(3,4),"python")
print(some.index("python"))---->1

any =(1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4])
print(any[2][2][1][15])
print(any.index(34))

Dictionary:
--------------
dictionary also known as "dict"
dict is a key:value pair,[key and value separated by :] and [pair is separated by comma
set of pairs are represented in {}

deepu_details = {"name":"deepu",1:2,(1,2):[3,4]}
print(deepu_details)--->{'name': 'deepu', 1: 2, (1, 2): [3, 4]}

key():
------
  syntax:print(dict.keys())                                                           
deepu_details ={"Name":"deepu",
                "age" :22,
                "Mobn":12345678,
                "pan":"geribsbb345"}
print(deepu_details.keys())----.dict_keys(['Name', 'age', 'Mobn', 'pan'])
                                                             
value():
-------------
 syntax:print(dict.values())                                                             
deepu_details ={"Name":"deepu",
                "age" :22,
                "Mobn":12345678,
                "pan":"geribsbb345"}
print(deepu_details.values())---->dict_values(['deepu', 22, 12345678, 'geribsbb345'])

teju_details ={"Name":"teja",
                "age" :45,
                "Mobn":123456789,
                "pan":"gpxyegewnsj"}
print(teju_details["Name"])--->teja
                                                            
                                                             
update():
------------
  used to add a new key : value pair into dict
  
teju_details ={"Name":"teja",
                "age" :45,
                "Mobn":123456789,
                "pan":"gpxyegewnsj"}
teju_details.update({"AADHAR":123456678987654})
teju_details["Name"] = "garikipati"
teju_details["age"] = 34
print(teju_details)
                                                             
clear():
-------                                                             
used to remove all the items in the dict

teju_details ={"Name":"teja",
                "age" :45,
                "Mobn":123456789,
                "pan":"gpxyegewnsj"}
teju_details.clear()
print(teju_details)--->{}                                                          




