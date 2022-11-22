import numpy as np
n = 16

lst0 = [0 for i in range(16*16-40)]
lst1 = [1 for i in range(40)]
lst = lst0+lst1
arr = np.array(lst)
# print(arr)
arr2 = np.random.permutation(arr)
# print(arr)
print(arr2.reshape(16,16))