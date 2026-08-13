def fn(ar):
    i=0;
    for j in range(len(ar)):
        if ar[j]!=0:
            ar[i],ar[j]=ar[j],ar[i];
            i+=1;

ar=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1];
fn(ar);
print(ar)