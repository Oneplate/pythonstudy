import random

def problem2_6():
    random.seed(431)
    for i in range(0,100):
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        num = num1+num2
        print(num)
