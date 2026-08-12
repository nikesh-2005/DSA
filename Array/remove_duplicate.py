def removeDuplicateBrute(ar):
    n=len(ar);
    index=0
    seen=set();
    for num in ar:
        if num not in seen:
            seen.add(num);
            ar[index]=num;
            index+=1;
    return index
                

def removeDuplicate(ar):
    n=len(ar);
    i=0;

    for j in range(1,n):
        if ar[i]!=ar[j]:
            i+=1;
            ar[i]=ar[j];
    return i+1

ar=[1,4,4,6,6,9,19];
k=removeDuplicate(ar);
print(k)
print(ar[:k])
