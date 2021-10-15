def hello():
    print ("Hello, world!")

def areacircle(radius):
    area = 3.14159 * radius**2
    print("The area of a circle of radius", radius, " is ", area)

def areatriangle(b,h):
    area = 0.5*b*h
    print("The area of a triangle with botton of ",b, " and height of ", h, " is ", area)

def FtoC (temp):
    # 5*(F-32)/9 = C #
    newtemp = 5*(temp-32)/9
    print ("The Fahrenhit temperature", temp, " is eqyuvalent to ", newtemp, end=' ')
    print (" degree Celcius")

def CtoF (temp):
    # (9*C/5) + 32 = F #
    newtemp = (9*temp/5)+32
    print ("The Celcius temprtature", temp, " is equivalent to ", newtemp, end=' ')
    print (" degree Fahrenheit")

def name():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    city = input("Enter the city you live in: ")
    state = input("Enter the state you live in: ")
    fullname = fname+" "+lname
    place = city+", "+state
    print ("Your name is: ", fullname)
    print ("Your live in: ", place)

print("############################")
print("#      Function manual     #")
print("#       h for hello()      #")
print("# c for areacircle(radius) #")
print("#  t for areatriangle(b,h) #")
print("#     F for FtoC(temp)     #")
print("#     C for CtoF(temp)     #")
print("#      Also q for quit     #")
print("#       n for name()       #")
print("############################")

while True:
    a = input()
    if a == 'h':
        hello()
    elif a == 'c':
        b = input()
        areacircle(float(b))
    elif a == 't':
        b = input()
        c = input()
        areatriangle(float(b),float(c))
    elif a == 'F':
        b = input()
        FtoC(float(b))
    elif a == 'C':
        b = input()
        CtoF(float(b))
    elif a == 'n':
        name()
    elif a == 'q':
        break
    else:
        continue
