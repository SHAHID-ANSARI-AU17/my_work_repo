# two different matrix show there sum.
mat1 = [[1,2,],[3,4]]
mat2 = [[2,3,],[4,5]]

row = len(mat1)
col = len(mat1[0])
for i in range(row):
    for j in range(col):
        print(mat1[i][j]+mat2[i][j],end=" ")
    print()