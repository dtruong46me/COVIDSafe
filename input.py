def instruction():
    print('Instruction:')
    print('1. Enter row and column to open a cell. Example: \'4 6\'')
    print('2. Enter row and column and letter \'F\' to open a cell. Example: \'4 6 F\'')
n = 16

import os
def clear():
    os.system('clear')

print(instruction())
while True:
    myInput = input().split()
    # if len(myInput)
    # print(myInput)
    if len(myInput) == 2:
        try:
            val = list(map(int,myInput))
        except ValueError:
            clear()
            print('Wrong input!')
            print(instruction())
            continue
    
    elif len(myInput) == 3:
        if myInput[2] != 'F' and myInput[2] != 'f':
            clear()
            print('Wrong input!')
            print(instruction())
        
        try:
            val = list(map(int, myInput[:2]))
        except ValueError:
            clear()
            print('Wrong input!')
            print(instruction())
            continue

        if val[0]<=0 or val[1]<=0 or val[1]>=n or val[1]>=n:
            clear()
            print('Wrong input!')
            print(instruction())
            continue

        # Get Row and Column from player's input
        row = val[0] - 1
        col = val[1] - 1