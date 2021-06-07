"""
sample input
1
5
1 2 3 4 5
sample output
6
# Print count of the sub array whose first element is odd and last element is even 
testcase = 1
n = 5 
Sub array are :
[1]
[1,2]
[1,2,3]
[1,2,3,4]
[1,2,3,4,5]
[2]
[2,3]
[2,3,4]
[2,3,4,5]
[3]
[3,4]
[3,4,5]
[4]
[4,5]
[5]
sub array that first and last array are odd as follow :->[1,2], [1,2,3,4], [3,4]
so the answer is - >  3

""" 

t = 1
n = 5
a = [1,2,3,4,5]
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        # print(res)
        if res[0]%2 == 0 and res[len(res)-1]%2 == 1: 
                count_main += 1
print(count_main)