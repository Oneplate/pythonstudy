def print_list(lis):
    if len(lis) == 0:
        print("How about inserting some entries to the list?")
    else:
        for a in lis:
            print(a, end = ' ')
    print("\nTotal", len(lis),"elements.")

mylis = []
while True:
    a = input("Insert something to the list. Type \'q\' for quit: ")
    if a == 'q':
        break
    elif a == ' ':
        mylis.append("Blankspace")
    else:
        mylis.append(a)

print_list(mylis)
