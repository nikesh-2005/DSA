#Brute force
def sortArray(ar):
    n=len(ar)
    zeroCounter=0
    oneCounter=0
    twoCounter=0

    for i in ar:
        if i==0:
            zeroCounter+=1
        elif i ==1:
            oneCounter+=1
        else:
            twoCounter+=1

    print(zeroCounter,oneCounter,twoCounter)
    for i in range(zeroCounter):
        ar[i]=0
    for i in range(zeroCounter,zeroCounter+oneCounter):
        print(i)
        ar[i]=1
    for i in range(zeroCounter+oneCounter,n):
        print(i)

        ar[i]=2

def sortArray2(ar):
    n=len(ar)

    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if ar[j]<ar[min]:
                min=j
        ar[min],ar[i]=ar[i],ar[min]

#Optimal approach

def sortArray(ar):
    i=0
    j=len(ar)

    while i<j:
        if ar[i]==0:
            i+=1
        if ar[j]==2:
            j-=1
        



ar=[1, 0, 2, 1, 0]
sortArray2(ar)
print(ar)