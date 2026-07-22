def PrintNames(N,name,count):
    if(count>N):
        return;
    print(name,end=" ");
    PrintNames(N,name,count+1);


N=5
PrintNames(N,"Nikesh",1);
