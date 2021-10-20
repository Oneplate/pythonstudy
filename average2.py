def is_digit(string):
    try:
        num = float(string)
        return True
    except:
        return False

def average(nlis):
    list_len = len(nlis)
    if list_len == 0:
        print("You should fill up your list with some numbers.")
        return True
    tot = 0
    for i in range(0, list_len):
        if not (is_digit(nlis[i])):
            print("YOU SHOULD FILL UP YOUR LIST WITH NUMBERS!")
            return False
        else:
            tot = tot+float(nlis[i])
            print(nlis[i], end = ' ')
    print("\nThe average is", tot/list_len)

mylis = []
while True:
    a = input("Input a number. \'q\' for quit.: ")
    if a == 'q':
        break
    else:
        mylis.append(a)
        
res = average(mylis)
if res == True:
    print("WhY nO nUmBeRs?")
elif res == False:
    print("Sorry, no strings allowed.")
else:
    pass
