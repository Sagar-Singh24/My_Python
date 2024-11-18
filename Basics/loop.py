# Loops

i=1
while(i<=50):
    if(i%2==0):
        print(i,"\t")
    i = i+1

while(i<=50):
    if(i%5==0 or i%7==0):
      print(i)
    i = i+1

sum = 0
while i<=5:
   sum = sum + i
   i = i + 1
print(sum)


list = [5,4,3,2,1]
length = len(list)
i=0
while i<length:
   print(list[i])
   i +=1


List1 = []
for i in list:
   List1.append(i*i)
print(List1)   


n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{n}*{i}= {n*i}")
   


