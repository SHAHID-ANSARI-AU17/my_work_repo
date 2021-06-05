"""
sample input
3
1 2 3
sample output
2

# Print count of sub array which have even sum
"""
n = 3 # user_input
a = [1,2,3]
count = 0
for i in range(n):
    res = []
    for j in range(i,n):
        res.append(a[j])
        print(res)
        if sum(res)%2==0:
            count +=1
print(count)
