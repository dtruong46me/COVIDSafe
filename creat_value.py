import numpy as np
n = 16
virus = 40

lst0 = [0 for i in range(n*n-virus)]
lst1 = [-1 for i in range(virus)]

# Place Virus randomly using numpy.permutation
arr = np.array(lst0+lst1)
arr2 = np.random.permutation(arr)
arr3 = arr2.reshape(n,n)
values = arr3.tolist()

# Set values
for row in range(n):
    for col in range(n):

        # Skip if this cell is virus
        if values[row][col] == -1:
            continue
        
        if row > 0 and values[row-1][col] == -1:
            values[row][col] += 1

        if col > 0 and values[row][col-1] == -1:
            values[row][col] += 1
        
        if row < n-1 and values[row+1][col] == -1:
            values[row][col] += 1
        
        if col < n-1 and values[row][col+1] == -1:
            values[row][col] += 1

        if row > 0 and col > 0 and values[row-1][col-1] == -1:
            values[row][col] += 1

        if row > 0 and col < n-1 and values[row-1][col+1] == -1:
            values[row][col] += 1

        if row < n-1 and col > 0 and values[row+1][col-1] == -1:
            values[row][col] += 1

        if row < n-1 and col < n-1 and values[row+1][col+1] == -1:
            values[row][col] += 1
 
# print(values)
    