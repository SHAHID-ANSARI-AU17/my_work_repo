# write a programe to calculate hcf.

# brute force method
a = 36
b = 48
c = []
d = []
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            c.append(i)
print_factors(a)       
print(c)

def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            d.append(i)

print_factors(b)       
print(d)

new_list = []
for i in c:
    if i in d:
        new_list.append(i)

print(new_list)

print(new_list[-1]) # for taking last no.