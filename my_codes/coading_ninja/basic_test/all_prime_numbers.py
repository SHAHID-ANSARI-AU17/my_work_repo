"""
Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).
Print the prime numbers in different lines.

"""
n = int(input())
for i in range(2, n + 1):
    for j in range(2, i):
        if (i % j) == 0:
               break
    else:
        print(i)