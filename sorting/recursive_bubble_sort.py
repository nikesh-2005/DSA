def bubbleSort(ar,n):
    if n<=1:
        return;
    isSwapped=False;
    for i in range(n-1):
        if ar[i]>ar[i+1]:
            ar[i],ar[i+1]=ar[i+1],ar[i];
            isSwapped=True;
    if not isSwapped:
        return;
    bubbleSort(ar,n-1);

ar=[4,2,76,2,1,7];
bubbleSort(ar,len(ar));
print(ar);