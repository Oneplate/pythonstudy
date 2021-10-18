def problem1_7():
    a = input("Enter the length of one of the bases: ")
    b = input("Enter the length of the other base: ")
    h = input("Enter the height: ")
    a = float(a)
    b = float(b)
    h = float(h)
    
    area = 0.5*(a+b)*h
    print("The area of a trapezoid with bases",a, "and", b, "and height",h, "is", area)
