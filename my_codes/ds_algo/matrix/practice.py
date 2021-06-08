mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

row = len(mat)
col = len(mat[0])

# for every element present in matrix
def matrix():
    for i in range(row):
        for j in range(col):
            print(mat[i][j],end = " ")
        print()
# matrix()


# for diagonal element
def diagonal():
    for i in range(row):
        for j in range(col):
            if i == j:
                print(mat[i][j],end= " ")
            print()
# diagonal()

# for anti diagonal
def anti_diagonal():
    for i in range(row):
        for j in range(col):
            if (i+j == row - 1): 
                print(mat[i][j],end=" ")
# anti_diagonal()

# matrix representation
# a = [[0 for i in range(3)]for j in range(3)]
# print(a)