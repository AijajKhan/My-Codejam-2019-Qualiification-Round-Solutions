{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 import math as make\par
\par
t=int(input())\par
\par
for x in range(0,t,1):\par
    n,l=map(int,input().strip().split())\par
    arr=list(map(int,input().strip().split()))\par
    temp=make.gcd(arr[0],arr[1])\par
    xanswer=[]\par
    xanswer.append(arr[0]//temp)\par
    xanswer.append(temp)\par
    \par
    for y in range(1,len(arr)):\par
        xanswer.append(arr[y]//xanswer[len(xanswer)-1]) #or xanswer[len(xanswer)-1]\par
    answer=set(xanswer)\par
    xanswer_c=sorted(answer)\par
    #answer=list(answer)\par
    #print(answer)\par
    mapper=\{\}\par
    for i in range(0,26,1):\par
        mapper[xanswer_c[i]]=chr(i+ord('A')) #we can also do ord('A')\par
   # print(mapper)\par
    mak=""\par
    for i in range(0,len(arr)+1,1):\par
        mak+=mapper[xanswer[i]]\par
    print("Case #\{\}: \{\}".format(x+1,mak))    \par
        \par
    \par
}
 