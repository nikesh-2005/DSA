# def leftRotate(ar):
#     firstEl=ar[0];
#     n=len(ar);
#     i=0;
#     j=1;

#     while j<n:
#         ar[i]=ar[j];
#         i+=1;
#         j+=1;
#     ar[n-1]=firstEl;

def leftRotate(ar):
    n=len(ar);
    firstEl=ar[0];
    for i in range(1,n):
        ar[i-1]=ar[i];
    ar[-1]=firstEl;

ar=[1,4,4,6,6,9,19];
leftRotate(ar);
print(ar)