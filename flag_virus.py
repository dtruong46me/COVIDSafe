# Position of virus that have been flagged
flags = []
virus = 40
row = 0
col = 0
n = 16
values = [[0 for i in range(n)] for j in range(n)]
while True:
    if len(flags) < virus:
        flags.append([row,col])
        values[row][col] = 'F'
        continue

    else:
        print('Flags finished')
        continue