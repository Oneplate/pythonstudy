# ExercisesModuleEnd1.py

def print_phrase():
    phrase = "Now is the time"
    print(phrase)

def favorite_sport(favorite):
    sport = "favorite"
    print("Your favorite sport is", sport)

def username(yourname):
    print("Your name is ", yourname)

def compare_numbers(x,y):
    if x == y:
        print("They are equal")
    else:
        print(x, " and ", y, " are not equal")

def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    print ("Counting from 5 through 100 in steps of 5")
    ct = 5
    while ct <= 100:
        print(ct, end = ' ')
        ct = ct+5

count_by_5()
