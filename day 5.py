SETS:
---------
-> A set is a collection of unique and unordered elements
-> duplicate values are not allowed
->items are not stored in index order
->represented in {}
->set is mutable

any ={1,2,2,3,4}
print(any)->{1,2,3,4}

any = {1,3,2,4,5}
print(any)->{1,2,3,4,5}
------------------------------------------------------------------------------
METHODS:
---------
i)union:
    it will give all values from 2 sets together in once
    syntax:variable_name.union(another var)

any = {1,2}
some = {3,4}
y ={5,6}
print(any | some)#--->{1,2,3,4}
print(any.union(some,y))#--->{1,2,3,4,5,6}
print(any|some|y)#--=>{1,2,3,4,5,6}
----------------------------------------------------------------------------------
ii)intersection:
    to get the common elements from both sets
    syntax : variable.intersection(another var)

any={1,2,2,3,4}
an = {3,2,30,80}
print(any.intersection(an))
any = {1,2,3}
an = {5,6,7}
print(any.intersection(an))#---->set()"because there are no same values from both sets
--------------------------------------------------------------------------------------
iii)difference():
   to get different values from the set 
   syntax:variable_name.difference(another var))
any = {1,2,2,3,4}
an = {3,26,89}
print(any - an)--->{1,2,4}
print(an.difference(any))--->{89,26}
---------------------------------------------------------------------------------------

 FUNCTIONS:
 -------------
 
 i)add():
    to add new elements into set ,we can add more than one value
    syntax : variable_name.add(value)
    
any = {1,2,2,3,4}
any.add(41)
print(any)-->{1,2,3,4,41}
any = {1,2,2,3,4}
any.add(4)
print(any)-->{1,2,3,4}(it will not add 4 since set already having it)
---------------------------------------------------------------------------------------------
ii)update():

    to add multiple elements into set
    synatx:variable_name.update([elements])

any = {1,2,2,3,4}
any.update([41,42])
print(any)#-->{1,2,3,4,41}
--------------------------------------------------------------------------------------------------
iii)sum():

any = {1,2,2,3,4}
print(sum(any))--->10 it will count duplicates only one time
--------------------------------------------------------------------------------------------------
iii)remove():
     used to remove value from the set but it will through (key)error if the element not in set

any = {1,2,2,3,4}
any.remove(4)
print(any)#---->{1,2,3}
any.remove(5)
print(any)#--->keyerror:5
----------------------------------------------------------------------------------------------------'''
     























     
