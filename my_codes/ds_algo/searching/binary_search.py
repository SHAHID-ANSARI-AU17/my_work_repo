def low_bs(a,t):
    l = 0 
    r = len(a)-1
    while l<=r:
        mid  = (l+r)//2
        if a[mid]==t:
            return mid
        elif a[mid] > t:
            r = mid-1
        else:
            l = mid +1
    return -1

a = [1,1,1,1,2,2,2,3,3,3,3,4,5,5,6,7,8]
t = 6
print(low_bs(a,t))
        
    
    
