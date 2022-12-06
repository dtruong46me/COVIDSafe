n = 16
virus_value = [['V' for i in range(n)] for j in range(n)]
# print(virus_value)
for ii in virus_value:
    print(ii)


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

for row in range(n):
    if (row<9):
        print(str('0'+str(row+1)), end = ' ')
    else:
        print(str(row+1), end = ' ')
    for col in range(n):
        print('|'+' '+virus_value[row][col], end = '')
    print('|')
