"""
class MinbalError(Exception):
    def __init__(self):
        self.minbal = 5000
    def __str__(self):
        return "Your balance is less than "+str(self.minbal)

def checkbal(x):
    if x >= 500:
        print("Your balance is ",x)
    else:
        raise MinbalError

checkbal(200)
"""
from new17 import *

def checkeli(age):
    if age >= 18:
        print("VOTE!!!!")
    elif age<=0:
        print("INVALID INPUT!!!")
    else:
        raise MinnorAgeError


age = int(input("Enter age::"))
checkeli(age)
#print(9/0)
#21-12-21
