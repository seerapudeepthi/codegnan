'''LIST COMPREHENSIONS:
-----------------------
this list comprehension offers a shortest syntax when moving on to create a new list from exisiting list
syntax : variable_name = [expression loop condition]

old = [1,2,3,4,5]
new = [so for so in old if so%2==0]
print(new)

old = [1,2,3,4,5]
new = [so if so%2!=0 else "even" for so in old]
print(new)

GENERATORS:
-----------
* generators in python are special type of itterable,allowing users to iterate over data efficiently without storing everything in memory
* they generate values lazily using yield keyword
* why to use generators:
    1)generators does not store the entire data set and memory,they generate values on the run time
    2)avoiding the unnecessary storage of data speed up execution
    3)also used in pipelines topic
*how it works:
    1)it looks like normal function but uses the yield keyword instead of return
    2)when the function is called ,it does not execute immediately.instead,it returns a generator object which can be iterated using loop or the next()function

1)def simple_gen():
    
    yield 1
    yield 2
    yield 3
    
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

2)
def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

3)
def sqr(num):
    result =[]
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))

4)'''
so = "quantum computing is an advanced field of technology that harness the laws of quantum"
any=""
for j in so:
    if j not in "AEIOUaeiou":
        any += j
print(any)


        

    
    





























