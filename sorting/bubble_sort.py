def bubbleSort(ar):
    n=len(ar);
    for i in range(n):
        for j in range(n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j];


ar=[2,5,6,26,2,9000,1,6];
bubbleSort(ar);
print(ar);