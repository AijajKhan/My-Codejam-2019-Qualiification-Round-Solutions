
t=int(input())

for z in range(0,t,1):
    n=input()
    y=int(n)
    n=n.replace('4','1')
    x=int(n)
    print("Case #{}: {} {}".format(z+1,x,y-x))
    
