def printNumbers(N):
    if N<1:
        return;
    print(N,end=" ");
    printNumbers(N-1);

#Using backtracking

def printNumbers2(N,current):
    if current>N:
        return;
    printNumbers2(N,current+1);
    print(current,end=" ");


N=10;
printNumbers(N);
print()
printNumbers2(N,1);
