import math as make

t=int(input())

for x in range(0,t,1):
    n,l=map(int,input().strip().split())
    arr=list(map(int,input().strip().split()))
    temp=make.gcd(arr[0],arr[1])
    xanswer=[]
    xanswer.append(arr[0]//temp)
    xanswer.append(temp)
    
    for y in range(1,len(arr)):
        xanswer.append(arr[y]//xanswer[len(xanswer)-1]) #or xanswer[len(xanswer)-1]
    answer=set(xanswer)
    xanswer_c=sorted(answer)
    #answer=list(answer)
    #print(answer)
    mapper={}
    for i in range(0,26,1):
        mapper[xanswer_c[i]]=chr(i+ord('A')) #we can also do ord('A')
   # print(mapper)
    mak=""
    for i in range(0,len(arr)+1,1):
        mak+=mapper[xanswer[i]]
    print("Case #{}: {}".format(x+1,mak))    
        
    