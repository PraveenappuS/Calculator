def add():
    print("After Performing Addition: ",op1+op2)

def sub():
    print("After Performing Subtract;ion: ")
    if op1>op2:
        print(op1 - op2)
    else:
        print(op2 - op1)

def mul():
    print(op1*op2)

def div():
    if op1>=op2:
        print(op1/op2)
    else:
        print(op2/op1)

def mod():
    if op1>=op2:
        print(op1%op2)
    else:
        print(op2%op1)

while True:
    op1 = float(input("Enter the First Number: "))
    op2 = float(input("Enter the Second Number: "))
    s = int(input("Choose the Number To perform operation: "))
    if s == 1:
        print("Addition:")
        add()
    elif s==2:
        print("Subtraction: ")
        sub()
    elif s == 3:
        print("Multiplication: ")
        mul()
    elif s == 4:
        print("Division: ")
        div()
    elif s == 5:
        print("Modulus: ")
        mod()
    else:
        print("Enter the valid Number.")