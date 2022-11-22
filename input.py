def instruction():
    print('Instruction:')
    print('1. Enter row and column to open a cell. Example: \'4 6\'')
    print('2. Enter row and column and letter \'F\' to open a cell. Example: \'4 6 F\'')
n = 16
print(instruction())
while True:
    myInput = input().split()
    # if len(myInput)
    # print(myInput)
    if len(myInput) == 2:
        try:
            val = list(map(int,myInput))
        except ValueError:
            print('Wrong input!')
            print(instruction())
            continue
    
    elif len(myInput) == 3:
        if myInput[2] != 'F' and myInput[2] != 'f':
            print('Wrong input!')
            print(instruction())
        
        try:
            val = list(map(int, myInput[:2]))
        except ValueError:
            print('Wrong input!')
            print(instruction())
            continue

        if val[0]<=0 or val[1]<=0 or val[1]>=n or val[1]>=n:
            print('Wrong input!')
            print(instruction())
            continue

        # Get Row and Column from player's input
        row = val[0] - 1
        col = val[1] - 1