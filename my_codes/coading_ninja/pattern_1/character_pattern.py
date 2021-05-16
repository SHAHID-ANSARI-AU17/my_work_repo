## Read input as specified in the question
## Print the required output in given format
n = int(input())
i=1
while i<=n:
    j=1
    char = chr(ord('A')+i-1)
    while j<=i:
        char1 = chr(ord(char)+j-1)
        print(char1,end='')
        j+=1
    i+=1
    print()
    
    
