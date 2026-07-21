import math
def Armstrong(Num):
    digits=len(str(Num));
    temp=Num;
    sum=0;
    while temp>0:
        ld=temp%10;
        temp=temp//10
        sum+=ld**digits;
    return sum==Num

Num=153;
if Armstrong(Num):
    print(f"{Num} is a armstrong number");
else:
    print(f"{Num} is not a armstrong number");
