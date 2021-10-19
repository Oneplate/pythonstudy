def is_digit(a):
    try:
        a = float(a)
        return True
    except:
        return False
    
def average(lis):
    if len(lis) == 0:
        print("Maybe you should fill up the list with some numbers")
    i = 0
    sum = 0
    for i in range(0,len(lis), 1):
        if not is_digit(lis[i]):
            print("YOU SHOULD FILL UP YOUR LIST WITH NUMBERS!")
            return False
        else:
            sum = sum+float(lis[i])
        i = i+1
    return sum/len(lis)

mylis = []
while True:
    a = input("Type a number. \'q\' for stop.: ")
    if a == 'q':
        break
    else:
        mylis.append(a)

ave = average(mylis)
if not (ave == False):
    print("Average is", ave, "and there are total", len(mylis), "numbers in the list.")
