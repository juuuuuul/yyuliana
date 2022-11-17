a=int(input())
b=int(input())
x1=0
y1=0
#def gcd(a,b):
 #   if a==0:
  #      return b
   # else:
    #    return gcd(b%a,a)
#print(gcd(a,b))
def gcd(a,b):
    if a==0:
        return b,0,1
    fcd,x,y=gcd(b%a,a)
    x1=y-(b//a)*x
    y1=x
    return fcd,x1,y1
print(gcd(a,b))
  
