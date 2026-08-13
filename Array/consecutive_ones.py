def consicutiveOnes(ar):
    res=0
    cur=0
    for i in ar:
        if i==1:
            cur+=1
        else:
            if cur>res:
                res=cur
            cur=0
    if cur>res:res=cur
    return res

ar=[1, 1, 0, 1, 1, 1]

print(consicutiveOnes(ar))
