"""
sample input
3
1 2 3
sample output

# Print count of sub array in which every element is odd
n = 3
array = [1,2,3]
Sub array are :
[1] 
[1,2]
[1,2,3]
[2]
[2,3]
[3]

sub array that have only even no. are :-> sum are : [1], [3]
so the answer is - >  2

"""

n = 3
a = [1,2,3]
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        count_even = 0
        for q in res:
            if q%2!=0:
                count_even += 1
        if count_even == len(res):
            count_main += 1
print(count_main)


