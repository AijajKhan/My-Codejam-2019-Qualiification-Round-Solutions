{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9\par
t=int(input())\par
\par
for z in range(0,t,1):\par
    n=input()\par
    y=int(n)\par
    n=n.replace('4','1')\par
    x=int(n)\par
    print("Case #\{\}: \{\} \{\}".format(z+1,x,y-x))\par
    \par
}
 