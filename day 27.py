DATA ANALYSIS:
______________

this is process of inspecting,cleaning,transforming,and modeling data to discover useful insights...

2.diagnostic analysis:

    understanding causes
-----------------------------------------------------------------
3.predictive analysis:

    forecasting future outcomes
-----------------------------------------------------------------
4.prescriptive analysis:

    suggesting actions based on data
-----------------------------------------------------------------
why DA:
    
-> to improve decision making
-> detects trends and patterns
_______________________________________________________________________________________________________________________________________

NUMPY:

-> numpy is numerical python
-> this python library for numerical computing.it provides support for multiple dimensional arrays,and linear algebra operations,making it essential for data analysis...

using numpy in DA:

-> improved performance
-> simplify complex operations
-> easy data manipulation...

import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)

import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[5,6,7,8]])
print(arr_1)


import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(2,4)
print(reshaped)
________________________________________________________________________________________________________
MATHEMATICAL OPERATIONS USING ARRAY:

import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1 + 5)

import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1 - 5)
_____________________________________________________________________________________________________
import numpy as np
arr_1 = np.array([[1,2],[3,4]])
arr_2 = np.array([[5,6],[7,8]])
print(np.dot(arr_1 , arr_2))

import numpy as np
arr_1 = np.array([[10,20,30]])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)

import numpy as np
arr_1 = np.array([[10,20,30]])
copy_dee = arr_1.copy()
arr_1[0] = 200
print(copy_dee)
print(arr_1)
_______________________________________________________________________________________________________
PANDAS:

->the pandas is a powerful data manipulation and analysis library...
->where it provides data structure like series and datframes for efficiency data handling...

import pandas as pd
any = pd.Series([2999,3999,50000,4999,1999],index = ["ear buds","smartphone","lap","watch","footware"])
print(any)

METHODS:
1)mean()
2)sum()
3)max()
4)min()
5)apply()
6)map()
______________________________________________________________________________________________________________
DATA FRAMES:

import pandas as pd
data = {'product':['Earbuds','smartphone','lap','watch','footware'],
        'brand':['noise','oneplus','hp','bolt','nike'],
        'price':[1599,53999,1999,3999,499],
        'stock':[50,15,25,40,70]
        }
dip = pd.DataFrame(data)
print(dip)


























































