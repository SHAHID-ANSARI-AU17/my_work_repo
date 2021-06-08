# given a matrix generate its transpose matrix

mat = [[1,2,3],[4,5,6]]

row  = len(mat)
col = len(mat[0])

new_mat = [[0,0],[0,0],[0,0]]
for i in range(row):
    for j in range(col):
        mat[i][j] = new_mat[j][i]
print(new_mat)
