Matplotlib:
_________________

->this is a library in python for data visualization,allowing users to create a variety of plots...

Basic structure of Matplotlib:
________________________________

1)figure
2)axes
3)grid
4)title
5)legend

BAR GRAPH:
_________________

import matplotlib.pyplot as plt
sales = ['A','B','c']
values = [25,30,45]
plt.bar(sales,values,color ='yellow',edgecolor = 'black')
plt.xlabel('car models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

LINE PLOT:
_________________

import matplotlib.pyplot as plt
sales = ['A','B','c']
values = [25,30,45]
plt.plot(sales,values,color = 'blue',linestyle = '-.',marker = "p", markerfacecolor = "lightblue")
plt.xlabel('car models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

import matplotlib.pyplot as plt
overs = [1,2,3,4,5]
score = [5,9,17,8,10]
plt.plot(overs,score,color = 'orange')
plt.title('score card')
plt.xlabel('overs')
plt.ylabel('score')
plt.show()


PIECHART:
_________

import matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [35,7,15]
plt.pie(students,labels = subjects,autopct = '%1.1f%%',colors = ["blue","green","pink"])
plt.legend(subjects)
plt.title('students in courses')
plt.show()

SCATTER:
__________

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,15,18,20,13]

plt.scatter(x,y,color = "green")
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('y values')
plt.show()

HISTOGRAM PLOT:
_________________

import matplotlib.pyplot as plt
x = [10,15,18,20,15,11]
plt.hist(x,color = "lightblue",edgecolor = "black")
plt.title('histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()'''














































