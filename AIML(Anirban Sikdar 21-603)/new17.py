def fibonaci(num):
    x = 1
    for i in range(1,num+1):
        x = x*i

    return x

def power(x,y):
    z = x**y
    return z
    
class MinnorAgeError(Exception):
    def __init__(self):
        self.age = 18
    def __str__(self):
        return "You are not Eligilble age bar is -->" + str(self.age)

print(fibonaci(9))
#21-12-21
