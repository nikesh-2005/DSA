def secondSmallestAndLargest(ar):
    if len(ar)<2:
        return -1,-1;

    max=float('-inf');
    min=float('inf');
    secMax=float('-inf');
    secMin=float('inf');
    for el in ar:
        if el>max:
            secMax=max;
            max=el;
        elif el>secMax and el<max:
            secMax=el;
        if el<min:
            secMin=min;
            min=el;
        elif el<secMin and el>min:
            secMin=el
    return secMin,secMax

ar = [10, 5, 2, 2]
secMin,secMax=secondSmallestAndLargest(ar);
print(secMax);
print(secMin);
