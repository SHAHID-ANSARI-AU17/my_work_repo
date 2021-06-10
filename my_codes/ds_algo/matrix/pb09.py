# print the ssum of the upper matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]

row  = len(mat)
col = len(mat[0])
sum = 0
for i in range(row):
    for j in range(col):
        if i <= j:
            sum += mat[i][j]
print(sum)
    
