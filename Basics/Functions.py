#Functions
#In-build Function

a = -45
print(abs(a))
print(bin(a))
print(bool(a))

str1 = "Ram"
print(str1.upper())
print(str1.lower())
print(str1.endswith("r"))
print(str1.capitalize())
print(str1.replace("R","r"))

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
def addition(a,b):
    sum = (a+b)
    return a+b
sum = addition(a,b)
print("The sum is :",sum)


a = int(input("Enter number:"))
def evenodd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")    
evenodd(a)        


addition = lambda a,b: a+b
print(addition(2,3))

mul = lambda a,b,c: a*b*c
print(mul(2,4,7))

min = lambda a,b: b if a>b else a
print(min(4,5))

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
min = lambda a,b,c: a if (a<b & a<c) else b if(b<c) else c
print(min(a,b,c))


def fun(a,b,c):#Formal parameters+
    print(a,b,c)
fun(1,2,3)
fun(a=8,b=56,c=0)
fun(b=56,c=9,a=7)
#fun(a=5,4,7)
    

def fun(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
fun(1,2,3,d=4,e=5,f=6)

def fun(a,b,c=5):
    print(a+b+c)
fun(1,2)    

def fun(a,b,/,c,d):
    print("a=",a,"b=",b,"c=",c,"d=",d)
fun(1,2,c=3,d=4)

def fun(a,b,/,*,c,d):
    print(a , b ,c ,d )
fun(1,2,c=3,d=5)

def fun1(*args):
    print(args)
    print(sum(args))
fun1(2,6,4,5)

def fun(a,b,c):
    print(a,b,c)
a=(1,2,3)
fun(*a)
