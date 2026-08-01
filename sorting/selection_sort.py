def selectionSort(ar):
    for i in range(len(ar)-1):
        min=i;
        for j in range(i+1,len(ar)):
            if ar[min]>ar[j]:
                min=j;
        ar[i],ar[min]=ar[min],ar[i];

ar=[2,5,6,26,2,9000,1,6];
selectionSort(ar);
print(ar);