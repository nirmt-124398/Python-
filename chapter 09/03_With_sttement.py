f=open("file.txt")
print(f.read())
f.close()

# It can also be written as:
with open("file.txt") as f:
    print(f.read())

# No neddd to close the file .it wil automatically close.