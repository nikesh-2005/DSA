def isPallindrome(str):
    temp="";
    for i in range(len(str)-1,-1,-1):
        temp+=str[i];
    
    return temp==str
        

def isPallindrome2(str):
    left,right=0,len(str)-1;

    while left<right:
        if not str[left].isalnum():
            left+=1;
        elif not str[right].isalnum():
            right-=1;
        elif str[left].lower!=str[right].lower:
            return False;
        else:
            left+=1;
            right-=1
    return True;

        
#Using recursion 

def isPallindrome3(str,left,right):
    if right<=left:
        return True;


    if str[left]!=str[right]:
        return False;
    return isPallindrome3(str,left+1,right-1);


str="ABBA";
if isPallindrome3(str,0,len(str)-1):
    print(f"{str} is a pallindrome");
else:
    print(f"{str} is not a pallindrome");
    