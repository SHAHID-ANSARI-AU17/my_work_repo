"""
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
"""
def checkPalindrome(num):
    rev = 0
    while num > 0:
        rem = num%10
        rev = (rev*10)+rem
        num = num//10
    return rev
   
        
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')