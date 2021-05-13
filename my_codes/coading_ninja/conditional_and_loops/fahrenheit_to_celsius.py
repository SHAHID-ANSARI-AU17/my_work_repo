"""
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
"""
# Read input as sepcified in the question
# Print output as specified in the question

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
##      print(val1, " ", val2)

S = int(input())
E = int(input())
W = int(input())

for i in range(S,E+1,W):
    result = int((i - 32)*(5/9))
    print(i," ",result)