"""
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE

"""
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i<=n:
    j = 1
    ch = ord('A')+n-i
    while j<=i:
        print(chr(ch+j-1),end='')
        j+=1
    i+=1
    print()