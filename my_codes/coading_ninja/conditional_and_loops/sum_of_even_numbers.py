"""
Given a number N, print sum of all even numbers from 1 to N.

"""
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = 0
for i in range(2,n+1,2):
    a += i
print(a)