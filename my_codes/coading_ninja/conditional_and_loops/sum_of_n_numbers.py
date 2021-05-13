"""
Given an integer n, find and print the sum of numbers from 1 to n.
"""
# Read input as sepcified in the question
# Print output as specified in the question
n = int(input())
a = 0
for i in range(1,n+1):
    a += i
print(a)