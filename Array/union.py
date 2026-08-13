#Using set
def union(ar1,ar2):
    unionSet=set();

    for num in ar1:
        unionSet.add(num);
    for num in ar2:
        unionSet.add(num);

    return unionSet;



#using hashmap

def union2(ar1,ar2):
    unionDict={}

    for num in ar1:
        unionDict[num]=num;

    for num in ar2:
        unionDict[num]=num;
    ar=unionDict.keys();

    return ar;


#Optimal solution

def union3(ar1,ar2):
    n1=len(ar1)
    n2=len(ar2)
    j=0
    i=0
    unionAr=[]
    while i<n1 and j<n2:
    
        if ar1[i]==ar2[j]:
            if not unionAr or unionAr[-1]!=ar1[i]:
                unionAr.append(ar1[i])
            i+=1
            j+=1
        elif ar1[i]<ar2[j]:
            if not unionAr or unionAr[-1]!=ar1[i]:
                unionAr.append(ar1[i])
            i+=1
        elif ar1[i]>ar2[j]:
            if not unionAr or unionAr[-1]!=ar2[j]:
                unionAr.append(ar2[j])
            j+=1
    while i<n1:
        if not unionAr or unionAr[-1]!=ar1[i]:
            unionAr.append(ar1[i])
        i+=1

    while j<n2:
        if not unionAr or unionAr[-1]!=ar2[j]:
            unionAr.append(ar2[j])
        j+=1

    return unionAr;
    


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1,2, 3, 4, 4, 5, 11, 12]
print(union3(arr1,arr2))