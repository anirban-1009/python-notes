while True:#WHILE LOOP
    a = int(input("Enter the first number:"))#ASSIGNING NUMBERS
    b = int(input("Enter the second number:"))

    o = str(input("Enter the function:"))#ACCEPTING FUNTION TO BE PERFORMED

    if o == "add":#ADDITION
        print(a+b)
    elif o == "sub":#SUBSTRACTION
        print(a-b)

    elif o == "mul":#MULTIPLICATION
        print(a*b)
    elif o == "div":#DIVISION
        print(a/b)

    elif o == "mod":#MODULUS
        print(a%b)

    elif o == "pow":#POWER OF
        print(a**b)

    elif o == "own":#UNDEFNIED YET RETURNS A INT OF DIVISION SO FIGURE IT OUT
        print(type(a//b))
        print(a//b)
    else:
        print("Invalid function")


#AUTHOR-ANIRBAN SIKDAR
