# Q2) Given a matrix print its diagonal difference.
mat = [[1,2,3],[4,5,6],[0,8,9]]
row = len(mat)
col = len(mat[0])
diagonal = 0
anti_diagonal = 0
for i in range(row):
    for j in range(col):
        if i == j:
            diagonal += mat[i][j]
        if col-1 == i + j:
            anti_diagonal +=  mat[i][j]
print(diagonal-anti_diagonal)