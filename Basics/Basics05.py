temp1 = [1,2,["a","b"]]

#general copy
temp2 = temp1
print(temp2)

#shallow copy
temp3 = temp1.copy()

#deep copy
import copy
temp4 = copy.deepcopy(temp1)
print(temp4)
print("temp1 id = ",id(temp1))
print("temp1 id = ",id(temp2))
print("temp1 id = ",id(temp3))
print("temp1 id = ",id(temp4))

a = 25
b = float(a)
c = str(a)
print(a)
print(b)
print(c)

f = 25.0
f1 = int(f)
print(f)
print(f1)
complex = 5+0j
print(str(complex))

a1 = True
print(int(a1))

a2 = "29"
print(str(29))

a3 = "29"
print(float(29))

#print(complex(a3))
print(list(a3))
print(tuple(a3))
print(set(a3))
#print(dict(a3))

a4 = "abcabc"
print(list(a4))
print(tuple(a4))
print(set(a4))

a5 = [1,2,3]
print(str(a5))
print(list(a5))
print(tuple(a5))
print(set(a5))

a6 = (1,2,3)
print(str(a6))
print(list(a6))
print(tuple(a6))
print(set(a6))

a7 = ((3,(1,2)),(6,4))
print(dict(a7))

tup = (1,2,3)
temp1 = tup + (5,6,7)
print(temp1)

a8 = {1:2,3:4}
print(list(a8))
print(tuple(a8))