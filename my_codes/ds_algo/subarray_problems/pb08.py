"""
sample input
1
5
1 2 3 4 5
sample output
6
# Print count of the sub array whose first and last element are odd 
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
sub array that first and last array are odd as follow :-> [1], [1,2,3], [1,2,3,4,5], [3], [3,4,5], [5]
so the answer is - >  6

"""   # this code is absolutely correct but not working probrly compiler must have the problem.   
t = 1
n = 5
a = [1,2,3,4,5]
count_main = 0
# for i in range(n):
#     res = []
#     for j in range(i,n):
#         res.append(a[j])
#         print(res)
#         lenq = len(res)
#         if lenq == 1:
#             if res[0]%2 != 0:
#                 count_main += 1
#         if lenq > 1:
#             count2 = 0
#             for k in range(lenq):
#                 if k == 0:
#                     if a[k]%2!=0:
#                         count2 +=1
#                 if k == (lenq-1):
#                     if a[k]%2!=0:
#                         count2 +=1
#             if count2 == 2:
#                 count_main += 1
# print(count_main)


# second approach , first one was somehow wrong i dont understand how but wrong this one only take 160 steps istead of 270 to complete.
count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        print(res)
        count = 0
        length = len(res)
        if length == 1:
            if res[0]%2 == 1:
                count_main += 1
        else:
            if res[0]%2 == 1:
                count += 1
            if res[length-1]%2 == 1:
                count += 1
        if count == 2:
            count_main += 1
        
print(count_main)



# the best one is at there with only 87 steps, bhai moj krdi :) :) :) 

count_main = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        print(res)
        if res[0]%2 == 1 and res[len(res)-1]%2 == 1: 
                count_main += 1
print(count_main)
