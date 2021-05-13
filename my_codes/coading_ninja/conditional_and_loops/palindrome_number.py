"""
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
"""
def checkPalindrome(num):
    rev = 0
    while num > 0:
        rem = num%10
        rev = (rev*10)+rem
        num = num//10
    return rev
   
        
num = int(input())
temp = num
isPalindrome = checkPalindrome(num)
if(isPalindrome==temp):
    print('true')
else:
    print('false')