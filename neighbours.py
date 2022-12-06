from creat_value import *
visited = []
virus = [[' ' for i in range(n)] for j in range(n)]
def neighbours(row,col):
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
