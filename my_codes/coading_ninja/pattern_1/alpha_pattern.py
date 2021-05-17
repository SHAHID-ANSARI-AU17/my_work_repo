"""
Print the following pattern for the given N number of rows.
Pattern for N = 3
A
BB
CCC

"""
n = int(input())
i = 1
while i <= n:
    j = 1
    ch = ord('A')
    while j<=i:
        print(chr(ch+i-1),end='')
        j+=1
    i+=1
    print()

