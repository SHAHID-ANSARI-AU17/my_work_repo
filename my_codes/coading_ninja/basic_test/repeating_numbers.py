"""
Print the following pattern for the given number of rows.
Pattern for N = 3
1
23
4567
"""
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
a = 2
print('1')
while i <n:
    j=1
    while j <= 2**i:
        print(a,end='')
        a +=1
        if a > 9:
            a = 1
        j+=1
    i+=1
    print()
         