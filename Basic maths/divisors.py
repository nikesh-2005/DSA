import math;
def allDivisor(Num):
    divisors=[];
    for i in range(1,Num+1):
        if Num%i==0:
            divisors.append(i);
    return divisors


#Optimal solution

def allDivisorsOptimal(Num):
    divisors=[];
    for i in range(1,math.isqrt(Num)+1):
        if Num%i==0:
            divisors.append(i);
            if i!=Num/i:
                divisors.append(Num//i);
    divisors.sort();
    return divisors;


Num=36;
divisors=allDivisorsOptimal(Num);
print(f"divisors of {Num} are :" ,*divisors);
