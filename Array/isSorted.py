#brute force

def isSortedBrute(ar):
    n=len(ar);
    for i in range(n):
        for j in range(i+1,n):
            if ar[j]<ar[i]:
                return False;
    return True

def isSorted(ar):
    for i in range(len(ar)-1):
        if ar[i]>ar[i+1]:
            return False;
    return True;


ar=[1,4,4,6,8,9,19];
print(isSortedBrute(ar));