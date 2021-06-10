# print the ssum of the two matrix that given

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]

row  = len(mat1)
col = len(mat1[0])

for i in range(row):
    for j in range(col):
        print(mat1[i][j]+mat2[i][j],end=" ")
    print()
    