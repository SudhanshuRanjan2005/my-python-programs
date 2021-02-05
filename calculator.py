def add():
    a = int(input('Enter your first number = '))
    b = int(input('Enter your second number = '))

    c = a + b

    print('Sum of these number is', c)

def subtract():
    a = int(input('Enter your first number = '))
    b = int(input('Enter your second number = '))

    c = a - b

    print('Difference of these number is', c)

def multiply():
    a = int(input('Enter your first number = '))
    b = int(input('Enter your second number = '))

    c = a * b

    print('Product of these number is', c)

def divide():
    a = int(input('Enter your first number = '))
    b = int(input('Enter your second number = '))

    c = a / b

    print('Division of these number is', c)

def menu():
    while True:
        print('''Choose:
        1 for Addition
        2 for Subtraction
        3 for Multiplication
        4 for Division''')

        c = int(input('Enter your choice ='))

        if c==1:
            add()
        elif c==2:
            subtract()
        elif c==3:
            multiply()
        elif c==4:
            divide()

menu()