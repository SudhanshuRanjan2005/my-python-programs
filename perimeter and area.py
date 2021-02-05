# For finding area and perimeter of rectangle
def rectangle():
    l = int(input('Enter first side of Rectangle = '))
    b = int(input('Enter second side of Rectangle = '))

    # printing perimeter by using the formula for perimeter
    p = 2*(l+b)
    print('Perimeter of Rectangle is', p)

    # printing area by using the formula for area
    a = l*b
    print('Area of given Rectangle is', a)


# For finding area and perimeter of circle
def square():
    # to calculate the perimeter and area of square

    s = int(input('Enter side of square = '))

    # printing perimeter by using the formula for perimeter
    p = 4*s
    print('Perimeter of square is', p)

    # printing area by using the formula for area
    a = s*s
    print('Area of given square is', a)


# For finding area and perimeter of circle
def circle():
    # to calculate the perimeter and area of circle

    r = int(input('Enter radius of Circle = '))

    # printing perimeter by using the formula for perimeter
    p = 2*3.14*r
    print('Perimeter of Circle is', p)

    # printing area by using the formula for area
    a = 3.14*r*r
    print('Area of given circle is', a)


# For finding area and perimeter of triangle
def triangle():
    # to calculate the perimeter and area of triangle

    a = int(input('Enter the first side of triangle ='))
    b = int(input('Enter the second side of triangle ='))
    c = int(input('Enter the third side of triangle ='))

    # calculate the side "s" of triangle 
    s = (a+b+c)/2

    # printing perimeter by using the formula for perimeter
    p = a+b+c
    print('Perimeter of the given triangle is',p)

    # printing area by using the formula for area
    ar = 0.5*(s*(s-a)*(s-b)*(s-c))
    print('Area of the given triangle is',ar) 

def menu():
    while True:
        print('''Choose:
        1 for Rectangle
        2 for Square
        3 for Circle
        4 for Triangle''')

        c = int(input('Enter the choice form the above ='))
        if c==1:
            rectangle()
        elif c==2:
            square()
        elif c==3:
            circle()
        elif c==4:
            triangle()

        else : print('Enter between 1 to 4')

menu()
        