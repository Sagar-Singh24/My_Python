#python file handling is used to do the the different operation like reading
#writing,deleting and also open a file
#file = open("path_of_file","mode")
file = open("file.txt","r")
#print(file.read())
#print(file.read(5))
#print(file.readline())
#print(file.readlines())
file.close()
file = open("file.txt","w")
file.write("we are using write mode")
file.tell()
file.seek(12)
print(file.tell())
file = open("file.text","r+")
file.write("\n India")
with open("file.txt","r") as file:
   print(file.read())
