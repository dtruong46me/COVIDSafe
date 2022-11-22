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
