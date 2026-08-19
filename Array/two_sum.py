#Brute force
def twoSum(ar,target):
    n=len(ar)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if ar[i]+ar[j]==target:
                return [i,j]

    return [-1,-1]

#Better solution

def twoSum2(ar,target):

    n=len(ar)

    hashMap={}

    for i in range(n):

        dif=target-ar[i]

        if dif in hashMap:
            return [i,hashMap[dif]]
        hashMap[ar[i]]=i
    return [-1,-1]

#Optimal solution

def twoSum3(ar,target):

    n=len(ar)

    i=0
    j=n-1
    while i<j:
        tot=ar[i]+ar[j]
        if tot>target:
            j-=1
        if tot<target:
            i+=1
        if tot==target:
            return [i,j]

    return [-1,-1]

ar=[2,6,5,8,11]

print(twoSum3(ar,14))