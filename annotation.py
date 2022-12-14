from typeguard import typechecked

a: int =int(input())
b: int =int(input())
x1: int = 0
y1: int = 0

@typechecked
def gcd(a: int,b: int) -> tuple[int, int, int]:
    if a==0:
        return b,0,1
   
    fcd, x, y = gcd(b%a,a)
    x1: int=y-(b//a)*x
    y1: int=x
    return fcd, x1, y1
   
print(gcd(a,b))
