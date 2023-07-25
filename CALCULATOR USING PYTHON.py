while True:
    print("1.ADDITION")
    print("2.MULTIPLICATION")
    print("3.SUBTRACTION")
    print("4.DIVISION")
    print("5.EXIT")


    choice=int(input("Enter your choice:"))

    if choice==1:
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        c=a+b
        print("The sum of the given number is: " ,a+b)
    elif choice==2:
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        c=a*b
        print("The sum of the given number is: " ,a*b)
    elif choice==3:
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        c=a-b
        print("The sum of the given number is: ", a-b)
    elif choice==4:
        a=float(input("Enter the first number:"))
        b=float(input("Enter the second number:"))
        c=a/b
        print("The sum of the given number is: ", a/b)
    elif choice==5:
        print("Thankyou Goodbye :)")
        break


