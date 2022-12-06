import numpy as np
import os

def creat_board():
    global n
    n = 16
    print('    ', end = '')
    for i in range(n):
        if (i<9):
            print(str('0')+str(i+1), end = ' ')
        else:
            print(str(i+1), end = ' ')
    print()
    print('   ', end = '')
    for i in range(n):
        print('___', end = '')
    print('_')
    for j in range(n):
        if (j<9):
            print(str('0'+str(j+1)), end = ' ')
        else:
            print(str(j+1), end = ' ')
        for i in range(n):
            print('|', end = '__')
        print('|')
    print()


def creat_value():
    global n
    global virus
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


def check_over():
    global n
    global virus
    count = 0
    for row in range(n):
        for col in range(n):
            if True:
                pass
    if count == n*n-virus:
        return True
    else:
        return False


def clear():
    os.system('clear')


def neighbours(row,col):
    global values
    global virus
    global visited
    if [row,col] not in visited:
        visited.append([row,col])

        if values[row][col] == 0:
            virus[row][col] = values[row][col]

            if row>0:
                neighbours(row-1,col)
            elif col>0:
                neighbours(row,col-1)
            elif row<n-1:
                neighbours(row+1,col)
            elif col<n-1:
                neighbours(row,col+1)
            elif row>0 and col>0:
                neighbours(row-1,col-1)
            elif row<n-1 and col<n-1:
                neighbours(row+1,col+1)
            elif row>0 and col<n-1:
                neighbours(row-1,col+1)
            elif row<n-1 and col>0:
                neighbours(row+1,col-1)
        if values[row][col] != 0:
            virus[row][col] = values[row][col]


def instruction():
    print('Enter the value to open the cell:')
    print('Example: 3 4')
    print('Enter the value and letter \'V\' to marking the cell is virus:')
    print('Example: 4 5 V')


if __name__ == '__main__':
    n = 16
    virus = 40
    values = [[0 for i in range(n)] for j in range(n)]
    virus = [[' ' for i in range(n)] for j in range(n)]
    visited = []
    marking = []
    over = False
    creat_value()
    while not over:
        creat_board()
        user_input = input('Enter the row and column separated by space: ').split()

        if len(user_input) == 2:
            try:
                val = list(map(int,user_input))
            except ValueError:
                clear()
                continue
        
        elif len(user_input) == 3:
            if user_input[2] != 'V' and user_input[2] != 'v':
                clear()
                continue
            try:
                val = list(map(int,user_input[:2]))
            except ValueError:
                clear()
                continue
            
