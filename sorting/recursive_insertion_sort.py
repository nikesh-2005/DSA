def insertionSort(ar,n):
    if n>=len(ar):
        return;

    key=ar[n];
    j=n-1;
    while j>=0 and key<ar[j]:
        ar[j+1]=ar[j];
        j-=1;
    ar[j+1]=key;
    insertionSort(ar,n+1);

ar=[4,2,76,2,1,7];
insertionSort(ar,1)
print(ar);
