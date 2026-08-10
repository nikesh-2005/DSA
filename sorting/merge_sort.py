def mergeSort(ar,start,end):
    if start>=end:
        return;
    mid=(start+end)//2;
    mergeSort(ar,start,mid);
    mergeSort(ar,mid+1,end);
    merge(ar,start,mid,end);

def merge(ar,start,mid,end):
    low=start;
    high=mid+1;
    temp=[];
    while low<=mid and high<=end:
        if ar[low]<ar[high]:
            temp.append(ar[low]);
            low+=1;
        else:
            temp.append(ar[high]);
            high+=1;
    while low<=mid:
        temp.append(ar[low]);
        low+=1;
    while high<=end:
        temp.append(ar[high]);
        high+=1;

    for i in range(len(temp)):
        ar[start+i]=temp[i];

ar=[8,3,1,7,4];
mergeSort(ar,0,len(ar)-1);
print(ar);