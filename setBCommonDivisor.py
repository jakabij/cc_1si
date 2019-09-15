import sys

if sys.argv[1].lstrip("-").isdigit() and sys.argv[2].lstrip("-").isdigit():
    num_little=int(sys.argv[1])
    num_larger=int(sys.argv[2])
    cDivisor=-1
    if num_little>num_larger:
        tmp=num_little
        num_little=num_larger
        num_larger=tmp

    if num_little<0:
        for i in range(num_little,num_larger+1):
            if num_little%i==0 and num_larger%i==0:
                cDivisor=i
    else:
        for i in range(1,num_larger+1):
            if num_little%i==0 and num_larger%i==0:
                cDivisor=i

    if cDivisor==-1:
        print("No common divisor found! ")
    else:
        print("The greatest common divisor is:",cDivisor)
else:
    print("You have to add numbers!")
