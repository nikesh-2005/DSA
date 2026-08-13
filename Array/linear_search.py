def linearSearch(ar,num):
    for i,n in enumerate(ar) :
        if n==num:
            return i;
    return -1;


ar=[1, 2, 3, 4, 5];
print(linearSearch(ar,6))