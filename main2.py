import numpy as np
"""
We are learning and testing numpy here and its basics
"""
l1 = [1,2,3,4,5,6,7,8,9,10]
np_arr = np.array(l1)
print(np_arr[3]) # we access the element number 3
print(np_arr[2])
print(f"before changing {np_arr}")
np_arr[0] = 12
print(f"after changing {np_arr}")
"""
We create a array's slice item that which can be refering to the orginial array
"""
l2 = np_arr[3:5]
l2[0] = 100
print(np_arr)
l2 = [11,12,13,14,15,16,17,18,19,20]
l3 = [21,22,23,25,26,26,27,28,29,30]
np_arr2 = np.array([l1,l2,l3])
print(np_arr2)
print(np_arr2[1,2])
print(np_arr2.ndim)
print(np_arr2.shape) # this will tell us the number of columns and rows
