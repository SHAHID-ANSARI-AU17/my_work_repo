"""
sample input
3
1 2 7
sample output

# Print count of sub array in which every element is odd
n = 3
array = [1,2,7]
Sub array are :
[1] 
[1,2]
[1,2,7]
[2]
[2,7]
[7]

sub array that have only even no. are :-> sum are : [1,2,7], [2,7], [7]
so the answer is - >  3

"""
# first method 
n = 3
a = [1,2,7]
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        count_seven = 0
        for q in res:
            if q == 7:
                count_seven += 1
        if count_seven >= 1:
            count_main += 1
print(count_main)



# second method optimized
n = 3
a = [1,2,7]
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])  
        if 7 in res:
            count_main +=1
print(count_main)


