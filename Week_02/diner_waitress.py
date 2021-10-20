def diner_waitress():
    print("Hello, I'll be your waitress. What will you have?")
    mylis = []
    while True:
        a = input("\nmenu item: ")
        if a == "That's all":
            break
        mylis.append(a)
        
    print("You've ordered:")
    print(mylis)


diner_waitress()
    
