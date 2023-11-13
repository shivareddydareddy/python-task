x="whats 3 plus 4 plus 10 subtraction 3   multiply  4 divide 2"
y=x.split(" ")
c=[]
z=[]
a=["plus","multiply","subtraction","divide"]
 
for i in y:
    if i.isnumeric() == True:
        c.append(int(i))
for j in y:
    if j in a:
        z.append(j)
if len (c)<=len(z):
    print("duplicate operation")
elif len(c)==1:
    print(c[0])
else:
    r=c[0]
    for k in range(len(z)):
        if z[k]=="plus":
            r+=c[k+1]
        elif z[k]=="multiply":
            r*=c[k+1]
        elif z[k]=="subtraction":
            r-=c[k+1]
        elif z[k]=="divide":
            if c[k+1] !=0:
                r /=c[k+1]
            else:
                print("error:division by zero not possible")
    print(r)