import numpy as np
n = 16
virus = 40
lst0 = [0 for i in range(n*n-virus)]
lst1 = [1 for i in range(virus)]
lst = lst0+lst1
arr = np.array(lst)
# print(arr)
arr2 = np.random.permutation(arr)
# print(arr)
arr3 = arr2.reshape(16,16)
# print(arr2)
# print(arr3)
my_lst = arr3.tolist()
print(my_lst)