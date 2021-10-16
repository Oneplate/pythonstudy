def hello():
    print ("Hello, world!")

def areacircle(radius):
    if radius.isdigit():
        radius = float(radius)
        area = 3.14159 * radius**2
        print("The area of a circle of radius", radius, " is ", area)
    else:
        print("NO STRING INPUT ALLOWED")
        
def areatriangle(b,h):
    if (b.isdigit() and h.isdigit()):
        b = float(b)
        h = float(h)
        area = 0.5*b*h
        print("The area of a triangle with botton of ",b, " and height of ", h, " is ", area)
    else:
        print("NO STRING INPUT ALLOWED")
        
def FtoC (temp):
    # 5*(F-32)/9 = C #
    if temp.isdigit():
        temp = float(temp)
        newtemp = 5*(temp-32)/9
        print ("The Fahrenhit temperature", temp, " is eqyuvalent to ", newtemp, end=' ')
        print (" degree Celcius")
    else:
        print("NO STRING INPUT ALLOWED")

def CtoF (temp):
    # (9*C/5) + 32 = F #
    if temp.isdigit():
        temp = float(temp)
        newtemp = (9*temp/5)+32
        print ("The Celcius temprtature", temp, " is equivalent to ", newtemp, end=' ')
        print (" degree Fahrenheit")
    else:
        print("NO STRING INPUT ALLOWED")

def name():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    city = input("Enter the city you live in: ")
    state = input("Enter the state you live in: ")
    fullname = fname+" "+lname
    place = city+", "+state
    print ("Your name is: ", fullname)
    print ("Your live in: ", place)

def inches_to_feet(inches):
    if inches.isdigit():
        inc = int(inches)
        feet = inc//12
        extra = inc%12
        print(inc, " inches is ", feet, " feet and ", extra, " inches.")
    else:
        print ("NO STRING OR NEGATIVE INPUT ALLOWED")
        
print("############################")
print("#      Function manual     #")
print("#       h for hello()      #")
print("# c for areacircle(radius) #")
print("#  t for areatriangle(b,h) #")
print("#     F for FtoC(temp)     #")
print("#     C for CtoF(temp)     #")
print("#      Also q for quit     #")
print("#       n for name()       #")
print("#  i for inches_to_feet()  #")
print("############################")

while True:
    a = input()
    if a == 'h':
        hello()
    elif a == 'c':
        b = input()
        areacircle(b)
    elif a == 't':
        b = input()
        c = input()
        areatriangle(b,c)
    elif a == 'F':
        b = input()
        FtoC(b)
    elif a == 'C':
        b = input()
        CtoF(b)
    elif a == 'n':
        name()
    elif a == 'i':
        b = input()
        inches_to_feet(b)
    elif a == 'q':
        break
    else:
        continue
