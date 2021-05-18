"""
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
Input format :
Integer x
"""
## Read input as specified in the question.
## Print output as specified in the question.
x = int(input())
a = 1
c = 1
while c<=x:
    b = (3*a)+2
    if b%4 != 0:
        print(b,end=' ')
        c+=1
    a +=1
    
    
