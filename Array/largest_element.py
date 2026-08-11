def largestElement(ar):
    max=ar[0];
    for el in ar:
        if el>max:
            max=el;
    return max;

ar=[4,6,2,7,11,900,9];
print(largestElement(ar));