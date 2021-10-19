def who_is_there(lis):
    if "bear" in lis:
        print("There's a bear")
    if "lion" in lis:
        print("There's a lion")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers")
    if "daisy" in lis and "iris" in lis:
        print("There are at least two flowers")
    if "donkey" in lis:
        print("There is a donkey")
    if "horse" not in lis:
        print("There is no horse in the list")
    print ("The list has", len(lis), "items")

lis = []
while True:
    print("Type \'q\' to end the loop")
    a = input("Insert the element you want to put in the list: ")
    if a == 'q':
          break
    else:
        lis.append(a)
        
who_is_there(lis)

i = 0
print("We have", end = ' ')
while i<len(lis):
    print(lis[i], ",", end = ' ')
    i = i+1
print("as an element for the list.")
