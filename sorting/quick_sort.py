def quickSort(ar,low,high):
    if low>=high:
        return;
    pivot=quick(ar,low,high);
    quickSort(ar,low,pivot-1);
    quickSort(ar,pivot+1,high);


def quick(ar,low,high):
    pivot=ar[high];

    i=low-1;
    for j in range(low,high):
        if ar[j]<=pivot:
            i+=1;
            ar[i],ar[j]=ar[j],ar[i];
    ar[i+1],ar[high]=ar[high],ar[i+1];
    return i+1


ar=[2,9,4,7,6,4,1];
quickSort(ar,0,len(ar)-1);
print(ar)
