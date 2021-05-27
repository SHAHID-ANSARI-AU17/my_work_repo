# Q2. Write a program to calculate a**b.

a = 3
b = 4
# by brute force method.
print(a**b)

# by iterative method
c=1
for i in range(b):
    c *=a
print(c)

# by recursive
def power(a,b):
    if b == 0:
        return 1
    else:
        return a*power(a,b-1)

print(power(a,b))
