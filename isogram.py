#s="erty --- bhgf"
def isogram(s):
    for i in s:
        if i ==" " or i=="-":
            continue
        b=s.count(i)
        if b>1:
            return False
            break
            
        else:
            return True
            break
s="ertu  --hgf"
print(isogram(s))
