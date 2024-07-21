# Write to file.txt (will create a new file or overwrite existing one)
f = open("file.txt", "w")
f.write("HELLO THIS IS writnging \n")
f.write("HELLO THIS IS writnging \n")
f.close()

# Append to file.txt
str = "This is AGI"
f = open("file.txt", "a")
f.write(str)
f.close()
