num1=input("Enter a number (or a letter to exit): ")

while num1.isdigit():
    num1=int(num1)
    operator=input("Enter an operation: ")
    num2=int(input("Enter another number: "))
    if operator=="+":
        print("Result: ",num1+num2)
    elif operator=="-":
        print("Result: ",num1-num2)
    elif operator=="*":
        print("Result: ",num1*num2)
    elif operator=="/":
        print("Result: ",num1/num2)
    else:
        print("Take attention for the input of the operator!")
    
    num1=input("\nEnter a number (or a letter to exit): ")
