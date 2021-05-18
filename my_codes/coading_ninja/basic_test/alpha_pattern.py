"""
Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
"""
## Read input as specified in the question.
## Print output as specified in the question.
n  = int(input())
i = 1
ch = ord('A')
while i <=n:
    j=1
    while j<=i:
        print(chr(ch+i-1),end='')
        j+=1
    i+=1
    print()