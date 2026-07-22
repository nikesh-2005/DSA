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

ar=[1,2,3,4,5,6];
print(ReverseArray(ar));
print(ReverseArray2(ar));
