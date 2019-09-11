import random

statement1=1
statement2=1
while statement1==1 and statement2==1:
    attackNum=input("How many units attack: ")
    if attackNum.isdigit():
        statement1=0
        attackNum=int(attackNum)
        if attackNum<4 and attackNum>0:
            statement2=0
        else:
            statement1=1


statement1=1
statement2=1
while statement1==1 and statement2==1:
    deffendNum=input("How many units defend: ")
    if deffendNum.isdigit():
        statement1=0
        deffendNum=int(deffendNum)
        if deffendNum<3 and deffendNum>0:
            statement2=0
        else:
            statement1=1


diceA=[]
diceD=[]

for i in range(attackNum):
    diceA.append(random.randrange(1,7))

for i in range(deffendNum):
    diceD.append(random.randrange(1,7))

print("\nAttacker: ")
for i in range(len(diceA)):
    print(diceA[i]," ",end="")

print("")

print("Deffender: ")
for i in range(len(diceD)):
    print(diceD[i]," ",end="")

print("")

diceA.sort(reverse=True)
diceD.sort(reverse=True)
lostA=0
lostD=0

if len(diceA)==1:
    if diceD[0]>=diceA[0]:
        lostA+=1
    elif diceD[0]<diceA[0]:
        lostD+=1
else:
    for i in range(len(diceD)):
        if diceD[i]>=diceA[i]:
            lostA+=1
        elif diceD[i]<diceA[i]:
            lostD+=1

print("Attacker: Lost %d unit" %lostA)
print("Deffender: Lost %d unit" %lostD)
