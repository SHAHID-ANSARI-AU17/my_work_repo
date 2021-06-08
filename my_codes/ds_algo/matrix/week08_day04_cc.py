# Q1) print right diagonal :
mat = [[1,2,3,4],
       [4,5,6,7],
       [7,8,9,8]]
    
def anti_diagonal(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(row):
        for j in range(col):
            if col - 1 == i+j:
                print(mat[i][j],end = " ")
        print()
anti_diagonal(mat)
