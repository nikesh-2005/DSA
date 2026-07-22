def factorial(N):
    sum=1
    for i in range(1,N+1):
        sum*=i;
    return sum;

#Using recursion - parameters:

def factorial2(N,sum=1):
    if N==0:
        print(sum);
        return;
    factorial2(N-1,sum*N);

#using recursion function:

def factorial3(N):
    if N==0:
        return 1;
    return N*factorial3(N-1);

N=5
print(factorial(N));
factorial2(N,1);
print(factorial3(N));
