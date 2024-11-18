# String in depth
str1='You know what we are'
print(str1.swapcase())

str1='You know what we are'
print(str1.title())

str1='You know what we are'
print(str1.index("w"))

str1='You know what we are'
print(str1.index("o",2))
print(str1.index("o",str1.index("o")+1)) #same as above
print(str1.index("o",1))

str1='You know what we are'
print(str1.rindex("o"))

crush_list = ['jhilli','lilli','silli']
crush_list.insert(2,"monali")
print(crush_list)

print(crush_list.pop(1))

print(crush_list.remove("silli"))
print(crush_list)

print(crush_list.clear())
print(crush_list)

crush_list = ['jhilli','lilli','silli']
new = crush_list.copy()
print(new)

print(crush_list.count('silli'))

temp = [3,8,5,0,31,7]
temp.sort()
print(temp)

temp.sort(reverse = True)
print(temp)

temp1 =[2,4,"rrr",'c']
temp1.sort()  # it shows error
print(temp1)

crush_list = ['jhili','rupali','milli',"@","+"]
crush_list.sort()
print(crush_list)


