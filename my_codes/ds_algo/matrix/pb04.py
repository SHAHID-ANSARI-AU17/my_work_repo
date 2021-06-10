# print the sum of matric the greater one.
mat1 = [[1,2,3,4],[0,5,6,1],[9,3,0,8]]
row1 = len(mat1)
col1 = len(mat1[0])
sum1 = 0
for i in range(row1):
    for j in range(col1):
        sum1+=mat1[i][j]

mat2 = [[8,8],[8,8]]
row2 = len(mat2)
col2 = len(mat2[0])
sum2 = 0
for i in range(row2):
    for j in range(col2):
        sum2+=mat2[i][j]

if sum1>sum2:
    print("Matrix 1 is greater: ", sum1)
else:
    print("Matrix 2 is greater: ",sum2)

