#Using parameters
def sumFunc(N,sum):

    if N<1:
        print(sum);
        return;
    sumFunc(N-1,sum+N);

#Using functions

def sumFunc2(N):
    if N==1:
        return 1;
    return N+sumFunc2(N-1);


sumFunc(5,0)
print(sumFunc2(5))
