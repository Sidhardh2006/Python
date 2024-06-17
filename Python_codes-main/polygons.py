# to print shapes using python functions

# 1. Triangle
def triangle(side=3):
    """assign the length of side to get a triangle
       if you assign a negative value
       you will get the triangle downwards"""
    n = side
    if n > 0:
        h = n - 1
        for i in range(1, n + 1):
            print(" " * h, end="")
            for j in range(i):
                if j == 0 or j == (i - 1):
                    print("# ", end="")
                elif i == n:
                    print("# ", end="")
                else:
                    print(" ", end=" ")
            print()
            h -= 1
    elif n < 0:
        n = -n
        h = n
        for i in range(n):
            print(" " * i, end="")
            for j in range(h):
                if j == 0 or j == (h - 1):
                    print("# ", end="")
                elif h == n:
                    print("# ", end="")
                else:
                    print(" ", end=" ")
            print()
            h -= 1


# 2.Square
def square(side=4):
    """assign the length of the side to get a square"""
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print("# ", end="")
            elif j == 0 or j == side - 1:
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()


# 3.Rectangle
def rectangle(length=5, breadth=8):
    """assign length and breadth of the rectangle to get a rectangle"""
    if length == breadth:
        print("if you want a rectangle \nplease enter different values for length and breadth")
    else:
        for i in range(length):
            for j in range(breadth):
                if i == 0 or i == length - 1:
                    print("# ", end="")
                elif j == 0 or j == breadth - 1:
                    print("# ", end="")
                else:
                    print(" ", end=" ")
            print()


# 4.Pentagon
def pentagon(side=5):
    """assign length of the side to get a pentagon
    please enter a value greater than 1"""
    h = side - 1
    for i in range(1, side + 1):
        print(" " * h, end="")
        for j in range(i):
            if j == 0 or j == (i - 1):
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()
        h -= 1
    for i in range(side - 1):
        for j in range(side):
            if i == side - 2:
                print("# ", end="")
            elif j == 0 or j == side - 1:
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()


# 5. Hexagon
def hexagon(side=6):
    """assign the length of the side to get a hexagon
    please enter a value greater than 1"""
    h = side
    c = 2 * side
    print(" " * h, end="")
    print("# " * side)
    for i in range(side - 1):
        h -= 1
        print(" " * h, end="")
        for j in range(c):
            if j == 0 or j == c - 1:
                print("# ", end="")
            else:
                print(" ", end="")
        print()
        c = c + 2
    h = 1
    c -= 2
    for i in range(1, side - 1):
        h += 1
        print(" " * h, end="")
        c = c - 2
        for j in range(c):
            if j == 0 or j == c - 1:
                print("# ", end="")
            else:
                print(" ", end="")
        print()
    print(" " * h, end=" ")
    print("# " * side)


# 6 . Heptagon
def heptagon(side=7):
    """assign the length of side to get a heptagon
    please assign a value greater than 2"""
    h = side
    c = 2 * side
    print(" " * h, end="")
    print("# " * side)
    for i in range(side - 1):
        h -= 1
        print(" " * h, end="")
        for j in range(c):
            if j == 0 or j == c - 1:
                print("# ", end="")
            else:
                print(" ", end="")
        print()
        c = c + 2
    for i in range(side - 1):
        for j in range(side * 2):
            if j == 0 or j == (side * 2) - 1:
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()
    n = side
    h = n
    for i in range(n):
        print(" " * (i * 2), end="")
        for j in range((h * 2) - 1):
            if j == 0 or j == ((h * 2) - 2):
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()
        h -= 1


# 7 . Octagon
def octagon(side=8):
    """assign the length of side to get an octagon"""
    h = side
    c = 2 * side
    print(" " * h, end="")
    print("# " * side)
    for i in range(side - 1):
        h -= 1
        print(" " * h, end="")
        for j in range(c):
            if j == 0 or j == c - 1:
                print("# ", end="")
            else:
                print(" ", end="")
        print()
        c = c + 2
    for i in range(side - 1):
        for j in range(side * 2):
            if j == 0 or j == (side * 2) - 1:
                print("# ", end="")
            else:
                print(" ", end=" ")
        print()
    for i in range(1, side - 1):
        print(" " * h, end="")
        c = c - 2
        for j in range(c):
            if j == 0 or j == c - 1:
                print("# ", end="")
            else:
                print(" ", end="")
        h += 1
        print()
    print(" " * h, end=" ")
    print("# " * side)
