string=input("Add the verbs: ")
verbs=string.split(" ")
pPForm=[]
modifiedVerb=[]
for i in range(len(verbs)):
    if verbs[i][-1]=="e" and verbs[i][-2]=="i":
        for j in range(len(verbs[i])-2):
            modifiedVerb.append(verbs[i][j])

        modifiedVerb.append("ying")
        pPForm.append(("".join(modifiedVerb)))
        modifiedVerb=[]

    elif verbs[i][-1]=="e":
        for j in range(len(verbs[i])-1):
            modifiedVerb.append(verbs[i][j])

        modifiedVerb.append("ing")
        pPForm.append(("".join(modifiedVerb)))
        modifiedVerb=[]
    
    elif not(verbs[i][-1]=="a" or verbs[i][-1]=="e" or verbs[i][-1]=="i" or verbs[i][-1]=="o" or verbs[i][-1]=="u") and (verbs[i][-2]=="a" or verbs[i][-2]=="e" or verbs[i][-2]=="i" or verbs[i][-2]=="o" or verbs[i][-2]=="u") and not(verbs[i][-3]=="a" or verbs[i][-3]=="e" or verbs[i][-3]=="i" or verbs[i][-3]=="o" or verbs[i][-3]=="u"):
        for j in range(len(verbs[i])):
            modifiedVerb.append(verbs[i][j])

        modifiedVerb.append(verbs[i][j]+"ing")
        pPForm.append("".join(modifiedVerb))
        modifiedVerb=[]
    else:
        for j in range(len(verbs[i])):
            modifiedVerb.append(verbs[i][j])

        modifiedVerb.append("ing")
        pPForm.append("".join(modifiedVerb))
        modifiedVerb=[]
                    
print("\n".join(pPForm))
