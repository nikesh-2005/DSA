import math;
def isPrime(Num):
    if Num==1:
        return False;
    
    for i in range(2,Num):
        if Num%i==0:
            return False
    
    return True;

#optimal solution

def isPrimeOptimal(Num):
    if Num==1:
        return False;
    
    for i in range(2,math.isqrt(Num)+1):
        if Num%i==0:
            return False;
    return True;
    


Num=2;
if isPrimeOptimal(Num):
    print(f"{Num} is a prime number");
else:
    print(f"{Num} is not a prime");