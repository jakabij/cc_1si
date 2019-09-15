def askNumbers(size):
    for i in range(size):
        numbers.append(input(""))
        while not(numbers[i].isdigit()):
            print("Write a number instead!")
            numbers.append(input(""))
        numbers[i]=int(numbers[i])



numbers=[]
N=input("How much number do you want to add? ")
while not(N.isdigit()):
    print("Write a number instead!")
    N=input("How much number do you want to add? ")
N=int(N)

print("Give the numbers by hitting ENTER!\n")
askNumbers(N)

print(numbers)

iterations=-1
while iterations<len(numbers):
    j=0
    while j<=(len(numbers)-2):
        if numbers[j]>numbers[j+1]:
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp
        j+=1
    iterations+=1
print(numbers)
