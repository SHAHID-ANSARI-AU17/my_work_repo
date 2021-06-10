# Given a 2-d array find the sum of all elements in the array.

mat = [[1,2,3],[1,2,3]]
row = len(mat)
col = len(mat[0])
sum = 0
for i in range(row):
    for j in range(col):
        sum += mat[i][j]
print(sum)