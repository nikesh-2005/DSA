def missingNumber(ar):
    n=len(ar)
    for i in range(1,n+1):
        found=False
        for num in ar:
            if i==num:
                found=True
                break
        if not found:
            return i
    return -1

def missingNumber2(ar):
    n=len(ar);
    hash=[0]*(n+2)
    for num in ar:
        hash[num]+=1 

    for i in range(1,len(hash)):
        if hash[i]==0:
            return i
    return -1
        

#optimal approach 1:

def missingNumber3(ar):
    n=len(ar)+1
    s=(n*(n+1))//2
    arSum=sum(ar);
    return s-arSum

ar=[1,5,4,6,3]
print(missingNumber3(ar))