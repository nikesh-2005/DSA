#Using forward tracking

def printNumbers(N,count):
    if(count>N):
        return;
    print(count,end=" ");

    printNumbers(N,count+1);

#Using backtracking 

def printNumbers2(N,current):
    if current<1:
        return;
    printNumbers2(N,current-1);
    print(current,end=" ");



N=10;
printNumbers(N,1);
print();
printNumbers2(N,N);
