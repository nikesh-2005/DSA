def gcd(Num1,Num2):
    gcd=1;

    for i in range(min(Num1,Num2),1,-1):
        if Num1 % i==0 and Num2 % i==0:
            gcd=i;
            break;
    return gcd;


#optimal solution

def gcdOptimal(Num1,Num2):
    while Num1>0 and Num2>0:
        if Num1>Num2:
            Num1=Num1%Num2;
        else:
            Num2=Num2%Num1;
    if Num1==0:return Num2;
    return Num1;
    
    

gcdVal=gcdOptimal(45,12);
print(gcdVal);