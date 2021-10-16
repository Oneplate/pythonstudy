
while True:
    print ("#####################################################")
    print ("# This is loop for comparison between three numbers #")
    print ("#  type a for positivity test and b for comparison  #")
    print ("#               also, type q for quit               #")
    print ("#####################################################")
    switch = input("Type a character: ")
    if switch == 'q':
        break
    
    x = input("Now, type the first number, x, you want to compare.: ")
    y = input("Second number, y.: ")
    z = input("Last number, z.: ")
    x = int(x)
    y = int(y)
    z = int(z)
    
    if switch == 'a':
        if x > 0:
            print ("x is positive")
        if y > 0:
            print ("y is positive")
        else:
            print ("y is not positive")
        if z > 0:
            print ("z is positive")
        elif z < 0:
            print("z is negative")
        else:
            print("z must be 0")
    elif switch == 'b':
        print("x is equal to y: ", x == y)
        print("x is not equal to y: ", x != y)
        print("x is equal to z: ", x == z)
        print("x is not equal to z: ", x != z)
    else:
        continue
    
