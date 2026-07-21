import math;

def digitsCount(Num):
    digits=0;
    
    while Num>0:
        Num=Num//10;
        digits+=1;
    return digits;


#Optimal solution

def digitsCountOptimal(Num):
    return int(math.log10(Num)+1)



num=int(input("Enter a number:"));
digits=digitsCountOptimal(num);
print(f"Number of digits in number {num} is {digits}");