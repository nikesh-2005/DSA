def insertionSort(ar:list[int]):
    for i in range(1,len(ar)):
        key=ar[i];
        j=i-1;
        while j>=0 and ar[j]>key:
            ar[j+1]=ar[j];
            j-=1;
        ar[j+1]=key

ar=[2,5,6,26,2,9000,1,6];
insertionSort(ar);
print(ar);