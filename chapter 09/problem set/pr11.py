#  Write a python program to rename a file to “renamed_by_ python.txt.
with open("old.txt") as f:
    content=f.read()
with open("renamed_old.txt","w") as f:
    f.write(content)
