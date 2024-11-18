# Conditional Statement

print(1==1)
print(1<2)
print(1>2)
print(2>=2)
print(3!=3)


temp = 40
print(temp)
print(True and False)

print( 2>0 and 2>0)
print(2>9 or 2>5 or 6>9)

print(not False)
print(not True)

print(4 & 4)
print(4|4)
print(4^5)

temp = 10
temp2 = temp
print( temp is temp2)

print(id(temp))

list1 = [1,2,3]
list2 = [1,2,3]

print(id(list1))
print(id(list2))

a=40
b=40
print(a==b)
print(a is b)
print(id(a))
print(id(b))


amount = int(input("Enter thr amount: "))
days = int(input("Enter no of days: "))
temp = amount *(2** (days//25))
print(temp)

i = 10

if(i>15):
    print("10 is greater")
else:
    print("10 is smaller")


a = int(input("Enter thr first number: "))
b = int(input("Enter thr second number: "))
c = int(input("Enter thr third number: "))
if(a>b):
   print("a is greatest number")
   if(b>c):
       print("b is greater than c less than a")
   else:
       print("c is smallest number")