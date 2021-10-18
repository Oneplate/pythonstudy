def problem1_4(miles):
    if miles.isdigit():
        miles = int(miles)
        feets = miles*5280
        print("There are",feets,"feet in",miles,"miles.")

a = input("miles? ")
problem1_4(a)
