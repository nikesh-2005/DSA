def reverseNumber(Num):
    revNum=0;
    while Num>0:
        ld=Num%10;
        Num=Num//10;
        revNum=(revNum*10)+ld;
    return revNum;


#using type  conversion
def reverseNumber_2(Num):
    str_digit=""
    while Num>0:
        ld=Num%10;
        Num=Num//10;
        str_digit+=str(ld);
    return int(ld);

num =reverseNumber(7754300);
print(num)