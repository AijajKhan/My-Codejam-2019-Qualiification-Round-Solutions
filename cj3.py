{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 import math\par
prime=[]\par
for y in range(2,10000,1):\par
        for u in range(2,y):\par
            if y%u==0:\par
                break\par
        else:\par
            prime.append(y)\par
\par
t=int(input())\par
for x in range(0,t,1):\par
    \par
    n,number=map(int,input().split())\par
    \par
    #-----------------------------------------------------------------------------\par
    new_prime=set()\par
    j=list(map(int,input().split()))\par
    for zedd in j:\par
        for zee in prime:\par
            if zedd%zee==0:\par
                new_prime.add(zee)\par
                \par
    #print(new_prime)\par
    \par
    #new_prime.sort()\par
    \par
    \par
   # new_prime=[]\par
    new_prime=list(new_prime)\par
    new_prime.sort()\par
    #print(new_prime)\par
    char=\{\}      \par
    char[new_prime[0]]='A'\par
    char[new_prime[1]]='B'\par
    char[new_prime[2]]='C'\par
    char[new_prime[3]]='D'\par
    char[new_prime[4]]='E'\par
    char[new_prime[5]]='F'\par
    char[new_prime[6]]='G'\par
    char[new_prime[7]]='H'\par
    char[new_prime[8]]='I'\par
    char[new_prime[9]]='J'\par
    char[new_prime[10]]='K'\par
    char[new_prime[11]]='L'\par
    char[new_prime[12]]='M'\par
    char[new_prime[13]]='N'\par
    char[new_prime[14]]='O'\par
    char[new_prime[15]]='P'\par
    char[new_prime[16]]='Q'\par
    char[new_prime[17]]='R'\par
    char[new_prime[18]]='S'\par
    char[new_prime[19]]='T'\par
    char[new_prime[20]]='U'\par
    char[new_prime[21]]='V'\par
    char[new_prime[22]]='W'\par
    char[new_prime[23]]='X'\par
    char[new_prime[24]]='Y'\par
    char[new_prime[25]]='Z'\par
    \par
    #print(new_prime)\par
    #print(char)\par
    \par
    answer=[]\par
    #number=int(input())\par
        \par
   # for i in range(0,number,1):\par
    \par
    for h in range(0,len(j),1):\par
        if h==0:\par
            for k in new_prime:\par
                if j[h]%k==0:\par
                    temp=j[h]/k\par
                    temp=math.floor(temp)\par
                    answer.append(char[k])\par
                    answer.append(char[temp])\par
                    #print(answer)\par
                    break\par
                       \par
                   \par
        else:\par
            div=j[h]/temp\par
            div=math.floor(div)\par
            #print(temp,div)\par
            answer.append(char[div])\par
            temp=j[h]/temp\par
            temp=math.floor(temp)\par
            #print(answer)\par
               \par
           \par
    print("Case #\{\}: \{\}".format(x+1,"".join(answer)))        \par
               \par
               \par
               \par
           \par
    \par
}
 