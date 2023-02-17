
"""temperature calculator"""

"""celsius para fahrenheit"""
def f (c):
    a=(c*1.8+32)
    return a    

# fahrenheit para celsius   
def c (f):
    a = ((f-32)/1.8)
    return a


s=str(input("valor "))
x=s.isnumeric()
if x:   
    x=float(s)
    d=f(x)
    print(d)
else:
     print("nao é um numero validoc")     


s=str(input("valor "))
x=s.isnumeric()
if x:   
    x=float(s)
    d=c(x)
    print(d)
else:
     print("nao é um numero validoc")     


