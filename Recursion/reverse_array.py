def ReverseArray(ar):
    n=len(ar);
    revAr=[0]*n;

    for i in range(n):
        revAr[i]=ar[n-1-i];

    return revAr;

def ReverseArray2(ar):
    n=len(ar);

    point1=0;
    point2=n-1;

    while point1<point2:
        
        ar[point1],ar[point2]=ar[point2],ar[point1];
        
        point1+=1;
        point2-=1;
    
    return ar;

#Using recursion

def ReverseArray3(ar, i, n):
    if i >= n // 2:
        return
    ar[i], ar[n - i - 1] = ar[n - i - 1], ar[i]
    ReverseArray3(ar, i + 1, n)




ar=[1,2,3,4,5,6];
print(ReverseArray(ar));
print(ReverseArray2(ar));
nums = [1, 2, 3, 4, 5]
ReverseArray3(nums, 0, len(nums))
print(nums)


