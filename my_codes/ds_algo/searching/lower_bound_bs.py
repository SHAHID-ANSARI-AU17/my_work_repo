def low_bs(a,t):
    l = 0 
    r = len(a)-1
    res = -1
    while l<=r:
        mid  = (l+r)//2
        if a[mid]==t:
            res = mid
            r = mid-1
        elif a[mid] > t:
            r = mid-1
        else:
            l = mid +1
    return res

a = [1,1,3,5,5,9,13,13,13,15,15,15,16,18,18]
t = 5
print(low_bs(a,t))
        
    
    
