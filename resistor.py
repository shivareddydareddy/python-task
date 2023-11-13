x=["yellow","green","blue","green"]                          #split given input using split
p={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
tolerance={"grey":0.05,"blue":0.25,"violet":0.1,"brown":1,"red":2,"green":0.5,"gold":5,"silver":10}
multiplier={"orange":"kilo","blue":"mega","red":"0","black":"00","yellow":"00000","green":" "}
rt =[]
secondlast=x[len(x)-2]                                       #second last color in str
the=multiplier.get(secondlast)                                #finding value for second last 


t=x[len(x)-1]                                                #finding last color in str

l=tolerance.get(t)                                           #finding its value

if len(x) ==1 or len(x) ==4 or len(x) == 5:    #traversing on if condition satifies
 
    for i in range(len(x)-2):                                    #loop to traverse upto lex(x) -2
        
        
    
        tx=p.get(x[i])                                            #finding values for those colors and adding them to empty list
    
        rt.append(tx)                                              
        
    for m in range (len(x)-2,len(x)-1):                           #travesing to last the len(x)-2 element to get multiplier value
    
    
        si=multiplier.get(x[m])
    
    for k in rt :
        print(k,end="")
    print(si,"ohms","+-",l,"tolerance")
else:
    print("undefined input")
