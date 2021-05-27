"""
Q1. Write a program to print the string backwards (by both methods).
Do the following questions recursively.

"""
# with iterative soln.
word = "hello"
for i in word[::-1]:
    print(i,end='')
print()

# with recursive
def rev(n):
    if len(n)==0:
        return n 
    else:
        return rev(n[1:]) + n[0]
n = "Hello"    
print(rev(n))