def count_a(lis):
    ct = 0
    for let in lis:
        if let == 'a':
            ct = ct+1
    print("There are", ct, "letter a in the list.")

mylis = []
while True:
    a = input("Insert an element for the list. Type \'q\'to quit.: ")
    if a == 'q':
        break
    else:
        mylis.append(a)
count_a(mylis)
