import math
prime=[]
for y in range(2,10001,1):
        for u in range(3,y):
            if y%u==0:
                break
        else:
            prime.append(y)

t=int(input())
for x in range(0,t,1):
    
    n,number=map(int,input().split())
    
    #-----------------------------------------------------------------------------
    x_prime=set()
    j=list(map(int,input().split()))
    for zedd in j:
        for zee in prime:
            if zedd%zee==0:
                x_prime.add(zee)
                x_prime.add(zedd//zee)
                if len(x_prime)==26:
                    break
                
    #print(new_prime)
    
    #new_prime.sort()
    
    
   # new_prime=[]
    new_prime=list(x_prime)
    new_prime.sort()
    print(new_prime)
    char={}      
    char[new_prime[0]]='A'
    char[new_prime[1]]='B'
    char[new_prime[2]]='C'
    char[new_prime[3]]='D'
    char[new_prime[4]]='E'
    char[new_prime[5]]='F'
    char[new_prime[6]]='G'
    char[new_prime[7]]='H'
    char[new_prime[8]]='I'
    char[new_prime[9]]='J'
    char[new_prime[10]]='K'
    char[new_prime[11]]='L'
    char[new_prime[12]]='M'
    char[new_prime[13]]='N'
    char[new_prime[14]]='O'
    char[new_prime[15]]='P'
    char[new_prime[16]]='Q'
    char[new_prime[17]]='R'
    char[new_prime[18]]='S'
    char[new_prime[19]]='T'
    char[new_prime[20]]='U'
    char[new_prime[21]]='V'
    char[new_prime[22]]='W'
    char[new_prime[23]]='X'
    char[new_prime[24]]='Y'
    char[new_prime[25]]='Z'
    
    #print(new_prime)
    #print(char)
    
    answer=[]
    #number=int(input())
        
   # for i in range(0,number,1):
    
    for h in range(0,len(j),1):
        if h==0:
            for k in new_prime:
                if j[h]%k==0:
                    temp=j[h]/k
                    temp=math.floor(temp)
                    answer.append(char[k])
                    answer.append(char[temp])
                    #print(answer)
                    break
                       
                   
        else:
            div=j[h]/temp
            div=math.floor(div)
            #print(temp,div)
            answer.append(char[div])
            temp=div
            temp=math.floor(temp)
            #print(answer)
               
           
    print("Case #{}: {}".format(x+1,"".join(answer)))        
               
               
               
           
    