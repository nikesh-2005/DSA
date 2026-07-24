from collections import defaultdict;

def frequency(ar):
    n=len(ar)
    visited=[False]*n;
    for i in range(n):
        if visited[i]:
            continue;
        count=1;
        for j in range(i+1,n):
            if ar[i]==ar[j]:
                count+=1;
                visited[j]=True;
        print(ar[i] ,count);


#Optimal solution

def frequency2(ar):
    freq_map =defaultdict(int);

    for i in range(len(ar)):
        freq_map[ar[i]]+=1;

    for key, value in freq_map.items():
        print(key, value);

ar=[5,11,2,3,11,5,4,3,2];
frequency2(ar);


