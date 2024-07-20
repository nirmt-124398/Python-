# Write a program to find out whether a given post is talking about “Harry” or not.

post=input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("This post is talking with Harry")

else:
    print("No harry")