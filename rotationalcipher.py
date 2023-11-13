a="CooL"
key =13
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
y="abcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in y:
        c=y.find(i)
        u=c+key
        #print(u)
        if u>26:
            z=u-26
            f=y[z]
            print(f,end="")
        else:
            print(y[u],end="")
    elif i in x:
        q=x.find(i)
        r=q+key
        if r>26:
            si=r-26
            de=x[si]
            print(de,end="")
        else:
            print(x[r],end="")