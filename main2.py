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
