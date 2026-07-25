from collections import defaultdict;

def highest_frequency(ar):
    n=len(ar);
    minEle=0;
    minCount=n;
    maxEle=0;
    maxCount=0;

    visited=[False]*n;

    for i in range(n):
        if visited[i]:
            continue;

        count =1;
        for j in range(i+1,n):
            if ar[i]==ar[j]:
                count+=1;
                visited[j]=True;
        
        if count>maxCount:
            maxCount=count;
            maxEle=ar[i];
        
        if count<minCount:
            minCount=count;
            minEle=ar[i];
    
    print("Highest frequency number:",maxEle ," ",maxCount);
    print("Lowest frequency number:",minEle ," ",minCount);



def highest_frequency2(ar):

    n=len(ar);

    freq_map=defaultdict(int);

    for i in range(n):
        freq_map[ar[i]]+=1;

    maxEle=0;
    minEle=0;
    maxCount=0;
    minCount=n;

    for num,count in freq_map.items():
        if count>maxCount:
            maxCount=count;
            maxEle=num;
        if count<minCount:
            minCount=count;
            minEle=num;
    print(f"The highest frequency number is {maxEle} : {maxCount}");
    print(f"The lowest frequency number is {minEle} : {minCount}");


ar=[1,5,3,7,5,8,1,6,1];
highest_frequency2(ar);