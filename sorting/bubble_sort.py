def bubbleSort(ar):
    n=len(ar);
    for i in range(n):
        didSwap=False;
        for j in range(n-i-1):
            if ar[j]>ar[j+1]:
                didSwap=True;
                ar[j],ar[j+1]=ar[j+1],ar[j];
        if  not didSwap:
            break;

ar=[2,5,6,26,2,9000,1,6];
bubbleSort(ar);
print(ar);