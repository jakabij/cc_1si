db=0
for i in range(1000,100,-1):
    if db==25:
        break
    if i%7==0 or i%9==0:
        print(i)
        db+=1
