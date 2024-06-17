"""this is the file of codes that i typed on my own!!!"""


def list_asc_sort(a):
    """assign a list to sort it in ascending order."""
    for i in range(len(a)):
        n = 0
        for j in a:
            if a[i] < j:
                a[i], a[n] = a[n], a[i]
            n += 1


def list_dec_sort(d):
    """assign a list to sort it in descending order."""
    for i in range(len(d)):
        n = 0
        for j in d:
            if d[i] > j:
                d[i], d[n] = d[n], d[i]
            n += 1


def is_prime(n):
    """assign a number to check if its a prime number."""
    if n < 2:
        print("not a prime number.")
        return None
    for i in range(2, n // 2):
        if n % i == 0:
            print("not a prime number.")
            break
    else:
        print("it is a prime number.")


def range_prime(a=None, n=None):
    """enter the starting and ending range to get the prime numbers and
    number of prime numbers in the range """
    if a is None:
        a = int(input("enter the starting range: "))
    if n is None:
        n = int(input("enter the ending range: "))
    count = 0
    for i in range(a, n + 1):
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            count += 1
            print(i, end=", ")
    print("\nthere are a total of {} prime numbers in the given range".format(count))


def nearest_prime(n=None):
    """assign a number to know its nearest prime."""
    if n is None:
        n = int(input("enter the number: "))
    d = n - 1
    lp = 0
    up = 2
    u = n + 1
    while d < n:
        if d < 2:
            break
        for i in range(2, (d // 2) + 1):
            if d % i == 0:
                break
        else:
            lp = d
            break
        d -= 1
    if lp > 0:
        while u > n:
            for i in range(2, (u // 2) + 1):
                if u % i == 0:
                    break
            else:
                up = u
                break
            u += 1
    if lp == 0:
        print("{} is the nearest prime to {}".format(up, n))
    elif up - n < n - lp:
        print("{} is the nearest prime to {}".format(up, n))
    elif n - lp < up - n:
        print("{} is the nearest prime to {}".format(lp, n))
    else:
        print("both {} and {} are nearest primes to {}".format(lp, up, n))


def fibonacci(limit=100):
    """give the limit to print the fibonacci series within that limit"""
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b


def armstrong_or_not(n):
    """assign a number to know if its an armstrong number or not"""
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))
    if s == n and s > 100:
        print("{} is an armstrong number".format(n))
        return True
    else:
        print("{} is not an armstrong number".format(n))
        return False


def range_armstrong(lower=100, upper=10000):
    """give the lower and upper limits to print the armstrong numbers within that range"""
    for i in range(lower, upper + 1):
        s = 0
        for j in str(i):
            s += int(j) ** len(str(i))
        if s == i:
            print(i, end=" ")


def even_or_odd(n):
    """assign a number to check if its an even number or odd number"""
    if n % 2 == 0 and n > 0:
        print("{} is an even number".format(n))
    else:
        print("{} is an odd number".format(n))


def factors(n):
    """assign a number to get its factors"""
    print("factors of {} are : ".format(n), end="")
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print(i, end=" ")
    print(n)


def multiples(n, limit=25):
    """assign a number to know its multiples"""
    i = 1
    print("the multiples of {} are ".format(n), end="")
    while i < limit:
        print(n * i, end=" ")
        i += 1
    print(".....")


def sum_natural_numbers(limit=100):
    """assign the limit to print the sum of natural number till that limit"""
    print("the sum of natural numbers up to {} is {}".format(limit, (limit / 2) * (limit + 1)))


def sum_of_nums(*nums):
    """assign multiple numbers to get the sum of that numbers"""
    s = 0
    for i in nums:
        s += i
    print("the sum of given numbers is {}".format(s))


def product(*nums):
    """assign multiple numbers to get the product of that numbers"""
    s = 1
    for i in nums:
        s *= i
    print("the product of given numbers is {}".format(s))


def triangle_or_not(a, b, c):
    """ assign the lengths of the three sides to know if a triangle is possible or not with given dimensions"""
    if a + b > c and b + c > a and a + c > b:
        print("triangle is possible with the given lengths...")
    else:
        print("triangle is not possible with the given lengths...")


def triangle_type(a, b, c):
    """assign the lengths of the three sides to know the type of the triangle"""
    if triangle_or_not(a, b, c):
        if a == b == c == a:
            print("we can form an equilateral triangle with the given measurements...")
        elif a == b or a == c or c == a:
            print("we can form an isosceles triangle with the given measurements...")
        else:
            print("we can form an scalene triangle with the given measurements...")
    else:
        print("any type of triangle cannot be formed with the given measurements...")


def triangle_area(a, b, c):
    """assign the length of three sides to get the area of the triangle"""
    if not triangle_or_not(a, b, c):
        return
    else:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return float("%.2f" % area)


def triangle_height_sides(a, b, c):
    """assign the length of the three sides to get the possible values of heights to the triangle"""
    area = triangle_area(a, b, c)
    h1 = 2 * area / a
    h2 = 2 * area / b
    h3 = 2 * area / c
    if h1 == h2 == h3:
        print("height = {}".format(h1))
    elif h1 == h2:
        print("heights can be {} and {}".format(h2, h3))
    elif h2 == h3:
        print("heights can be {} and {}".format(h2, h1))
    elif h1 == h3:
        print("heights can be {} and {}".format(h1, h2))
    else:
        print("heights can be {} , {} and {}".format(h1, h2, h3))


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


def pentagon(side=5):
    """assign length of the side to get a regular pentagon
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


def hexagon(side=6):
    """assign the length of the side to get a regular hexagon
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


def octagon(side=8):
    """assign length of side to get an octagon
    please assign a value greater than 3"""
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


def length_convertor(length=1, unit=None, convert=None):
    """converts the length"""
    if unit is None:
        print("light year, AU, mile, kilometer, yard, meter, decimeter, foot, inch, centimeter,"
              "millimeter, micrometer, nanometer, picometer")
        unit = input("type units of your length: ")
    if convert is None:
        print("light year, AU, mile, kilometer, yard, meter, decimeter, foot, inch, centimeter,"
              "millimeter, micrometer, nanometer, picometer")
        convert = input("type units you want to convert into: ")
    meter = {'light year': 9.46 * (10 ** 15), 'AU': 1.49 * (10 ** 11), 'mile': 1609.3, 'kilometer': 1000, 'yard': 1.093,
             'meter': 1, 'foot': 0.3048, 'decimeter': 0.1, 'inch': 0.0254, 'centimeter': 0.01, 'millimeter': 0.001,
             'micrometer': 10 ** -6, 'nanometer': 10 ** -9, 'picometer': 10 ** -12}
    print("{0} {1} = {2} {3}".format(length, unit, meter[unit] / meter[convert] * length, convert))
    return meter[unit] / meter[convert] * length


def time_converter(measure=1, unit=None, convert=None):
    """converts the time"""
    if unit is None:
        print("century, decade, year, month, week, hour, minute, day"
              " second, millisecond, microsecond, nanosecond, picosecond")
        unit = input("type units of your length: ")
    if convert is None:
        print("century, decade, year, month, week, hour, minute, day"
              " second, millisecond, microsecond, nanosecond, picosecond")
        convert = input("type units you want to convert into: ")
    time = {'century': 3.154 * (10 ** 9), 'decade': 3.154 * (10 ** 8), 'year': 3.154 * (10 ** 7),
            'month': 2.628 * (10 ** 6),
            'week': 604800, 'day': 86400, 'hour': 3600, 'minute': 60, "second": 1, "millisecond": 0.001,
            'microsecond': 10 ** -6, 'nanosecond': 10 ** -9, 'picosecond': 10 ** -12}
    print("{0} {1} = {2} {3}".format(measure, unit, time[unit] / time[convert] * measure, convert))
    return time[unit] / time[convert] * measure


def date_difference(start_date, end_date):
    """assign different date in 'dd-mm-yyyy' format to know the difference between these two dates"""
    date = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
            '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    if int(end_date[6:]) % 4 == 0:
        date['2'] = 29
    year = [int(start_date[0:2]), int(end_date[0:2]), int(start_date[3:5]), int(end_date[3:5])]
    if year[3] >= year[2]:
        if year[1] >= year[0]:
            month = year[3] - year[2]
        else:
            month = year[3] - year[2] - 1
        if year[1] - year[0] < 0:
            day = date[str(year[3] - 1)] + (year[1] - year[0])
        else:
            if year[1] - year[0] > 0:
                day = year[1] - year[0]
            else:
                day = 0
        year = int(end_date[6:]) - int(start_date[6:])
    else:
        if year[1] >= year[0]:
            month = (12 - year[2]) + year[3]
        else:
            month = ((12 - year[2]) + year[3]) - 1
        if year[1] - year[0] < 0:
            day = date[str(year[3] - 1)] + (year[1] - year[0])
        else:
            if year[1] - year[0] > 0:
                day = year[1] - year[0]
            else:
                day = 0
        year = int(end_date[6:]) - int(start_date[6:]) - 1
    print("{} years {} months {} days".format(year, month, day))