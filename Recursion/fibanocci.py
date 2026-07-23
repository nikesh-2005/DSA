def fibanoci(N):
    if N==0:
        print(0);
    elif N==1:
        print(0,1);
    else:

        ar=[0]*(N+1);
        ar[0],ar[1]=0,1;
        for i in range(2,N+1):
            ar[i]=ar[i-1]+ar[i-2];
        print(" ".join(str(num) for num in ar));

fibanoci(5)
    
