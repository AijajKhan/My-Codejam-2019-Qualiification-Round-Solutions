{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9\par
t=int(input())\par
\par
for z in range(0,t,1):\par
    temp=input()\par
    n=list(input())\par
    y=['0']*len(n)\par
    if n[0]=='S':\par
        y[0]='E'\par
    else:\par
        y[0]='S'\par
    \par
    for x in range(1,len(n),1):\par
        if n[x]==n[x-1]:\par
            y[x]=y[x-1]\par
        else:\par
            if n[x]=='S':\par
                y[x]='E'\par
            else:\par
                y[x]='S'\par
    print("Case #\{\}: \{\}".format(z+1,"".join(y)))\par
    \par
    \par
\par
}
 