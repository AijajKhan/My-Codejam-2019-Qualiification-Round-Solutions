
t=int(input())

for z in range(0,t,1):
    temp=input()
    n=list(input())
    y=['0']*len(n)
    if n[0]=='S':
        y[0]='E'
    else:
        y[0]='S'
    
    for x in range(1,len(n),1):
        if n[x]==n[x-1]:
            y[x]=y[x-1]
        else:
            if n[x]=='S':
                y[x]='E'
            else:
                y[x]='S'
    print("Case #{}: {}".format(z+1,"".join(y)))
    
    

