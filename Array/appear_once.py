def appearOnce(ar):
    for i in range(len(ar)):
        isExist=False
        for j in range(len(ar)):
            if ar[i]==ar[j] and i!=j:
                isExist=True
                break
        if not isExist:
            return ar[i]

#Better approach

def appearOnce2(ar):
    freq={}
    for i in ar:
        freq[i]=freq.get(i,0)+1

    for key,val in freq.items():
        if val==1:
            return key

def appearOnce3(ar):

    xorr=0
    for num in ar:
        xorr^=num

    return xorr

ar=[1,4,1,2,2]
print(appearOnce3(ar))