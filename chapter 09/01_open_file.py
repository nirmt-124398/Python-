f=open("file.txt")
f2=open("another_file.txt")

text2=f2.read() #reades entire file
print(text2)

text=f.readline()
while(text!=""):
    print(text)
    text=f.readline()
# SAME
# text=f.readline() #reads a line 
# print(text)
# text=f.readline()
# print(text)
# text=f.readline()
# print(text)
# text=f.readline()
# print(text=="")

f.close()