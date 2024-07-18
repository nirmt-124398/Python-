# The srtings are immutable i.e. if want to modify a string we have to creat a new string 

name="nirMit"

#Length function
print(len(name))

#ends and stats with
print(name.endswith("r"))
print(name.endswith("t"))
print(name.startswith("n"))
print(name.startswith("t"))

#count occurence of somethig
print(name.count("i"))

#Capitalise and casefold 1st letter
print(name.casefold()) #Returns whole string in lowwerCase
print(name.capitalize()) 

#Find a word

Full_name="hello  world"
print(Full_name.find("world"))
print(Full_name.find("World"))

#replace fun

sentence="Hello World, Its a nice World"
print(sentence.replace("World","Python")) # This changes all the occurences