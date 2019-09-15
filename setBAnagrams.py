import sys
file=open(sys.argv[1],"r")
list=file.readlines()

for i in range(len(list)):
    for j in range(len(list)):
        if not(list[i]==list[j]):
            if sorted(list[i])==sorted(list[j]):
                print(list[i],"is an anagram to",list[j])
