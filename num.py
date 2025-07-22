import numpy as np
#print(np.__version__)
l1 = [1,2,3,4]
l2 = ['dhruv',10] # this will not give error 
l3 = [[1,2,3],[4,5]] # this will give the error because the 2 D matrix should have the same number of rows and columns
np_arr = np.array(l2)
print(np_arr)
