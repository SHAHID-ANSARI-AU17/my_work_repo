# Q1) print right diagonal   # below code is works for both square or rectangle matrix.     
def anti_diagonal():
    mat = [[1,2,3,4],
        [4,5,6,7],
        [7,8,9,8]]

    row = len(mat)
    col = len(mat[0])

    for i in range(row):
        for j in range(col):
            if col - 1 == i+j:
                print(mat[i][j],end = " ")
        print()
# anti_diagonal()

# Q - 2) Write a program to print sum of border elements of a square Matrix  ## addtional i make this program to work also on rectangle

def border_element():
    mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

    row = len(mat)
    col = len(mat[0])
    sum = 0
    for i in range(row):
        for j in range(col):
            if i == 0 or i == (row-1) or j == 0 or j == (col-1):
                a = mat[i][j]
                # print(a,end = " ")
                sum+=a
            # print()
    print(sum)
# border_element()

# Q3) Write a function to return sum of rows of a matrix as a list.

def matrix_row():
    mat = [[1,2,3,4,],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    row = len(mat)
    col = len(mat[0])
    output_list = []
    for i in range(row):
        sum = 0
        for j in range(col):
            sum += mat[i][j]
        output_list.append(sum)
    print(output_list)    
# matrix_row()