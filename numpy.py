import numpy as np
#print(np.__version__)
l1 = [1,2,3,4]
l2 = ['dhruv',10] # this will not give error 
l3 = [[1,2,3],[4,5]] # this will give the error because the 2 D matrix should have the same number of rows and columns

"""
We are testing and learning the basic of numpy here
"""
np_arr = np.array(l1)
print(np_arr[3]) # we access the element number 3
print(np_arr[2])
print(f"before changing {np_arr}")
np_arr[0] = 12
print(f"after changing {np_arr}")
