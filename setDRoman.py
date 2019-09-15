num=input("The number: ")
roman=[]
while not(num.isdigit()):
    print("\nYou have to add a digit!")
    num=input("The number: ")

num=int(num)
for i in range(num//1000):
    roman.append("M")
num=num%1000
for i in range(num//500):
    roman.append("D")
num=num%500
for i in range(num//100):
    roman.append("C")
num%=100
for i in range(num//50):
    roman.append("L")
num%=50
for i in range(num//10):
    roman.append("X")
num%=10
for i in range(num//5):
    roman.append("V")
num%=5
for i in range(num):
    roman.append("I")

print("".join(roman))
    
