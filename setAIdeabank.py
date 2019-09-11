import sys

file=open("ideabank.txt","a")
idea=input("What is your new idea? ")
file.write(idea+"\n")
print("Your idea bank:")
file.close()

file=open("ideabank.txt","r")
j=1
for i in file:
    print("%d. " %j,i,end="")
    j+=1
print("")
file.close()
