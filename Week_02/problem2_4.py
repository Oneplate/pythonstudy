import random

def problem2_4():
    random.seed(70)
    mylis = []
    for i in range(0,10):
        p = random.random()
        mylis.append(30+p*5)
    print(mylis)
