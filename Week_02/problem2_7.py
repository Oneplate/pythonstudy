def problem2_7():
    a = input("Enter length of side one: ")
    b = input("Enter length of side two: ")
    c = input("Enter length of side three: ")
    a = float(a)
    b = float(b)
    c = float(c)
    s = 0.5*(a+b+c)
    area =(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a triangle with sides", a, b, c, "is", area)
