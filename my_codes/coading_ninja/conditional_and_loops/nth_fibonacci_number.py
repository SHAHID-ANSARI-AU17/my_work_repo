"""
Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
"""

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a,b = 0,1
if n < 0:
    print("Invalid input")
elif n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(1,n):
        c = a+b
        a = b
        b = c
    print(b)
        