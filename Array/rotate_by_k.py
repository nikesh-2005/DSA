def rightRotateByK(ar,k):
    n=len(ar);
    k=k%n;
    print(k)
    temp=ar[n-k:];

    for i in range(n-k-1,-1,-1):
        ar[i+k]=ar[i];
    for j in range(k):
        ar[j]=temp[j];


def leftRotateByK(ar,k):
    n=len(ar);
    k=k%n;
    temp=[]
    for i in range(k):
        temp.append(ar[i]);
    for j in range(k,n):
        ar[j-k]=ar[j];
    for j in range(n-k,n):
        ar[j]=temp[j-(n-k)];




ar=[1, 2, 3, 4, 5, 6, 7];
leftRotateByK(ar,2);
print(ar)