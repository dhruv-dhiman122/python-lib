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
l5 = [10,242,2433,22,422234,0,1222,11,54,345]
np_arr2 = np.array([l1,l2,l3,l5])
print(np_arr2)
print(np_arr2[1,2])
print(np_arr2.ndim)
print(np_arr2.shape) # this will tell us the number of columns and rows
print(np_arr.shape)
print(np_arr2.size) # this will give us the number of element within the array
print(np_arr2.dtype) # this will give us the data type of the array
l4 = ['dhruv',True, 12]
np_arr3 = np.array([l4])
print(np_arr3.dtype)
"""
We are starting from here to build basics array
"""
print(np.zeros(4))
print(f"an array with ones {np.ones(10)}")
#create a function that ask the zero to print either zero or one

def one_zero(option,size):
    if option == 0:
        print(np.zeros(size))
    else:
        print(np.ones(size))

print(np.empty(6))
print(np.empty(6))
print(np.arange(1,10,2))
print(np.linspace(0,10,num=2, dtype=np.int8))

print(f"we have the sorted array {np.sort(np_arr2)}")

test_sort = np.array([12,2,33,4,5,1,0,122,3,9])
print(f"the unsorted array is {test_sort}")
print(f"the sorted array is {np.sort(test_sort)}")
print(f"we are using the argsort function {np.argsort(test_sort)}")
print(f"We are using the lexsort function {np.lexsort(test_sort, axis=0)}")
x = np.array([1,2,3,5])
y = np.array([6,7,8,9,10])
print(f"We are using concentate function {np.concatenate((x,y),axis=None)}")
