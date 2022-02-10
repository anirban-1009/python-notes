 
#Write a python program to convert temperatures to and from celsius, farenheiht

#c/5 = f-(32-9)

"""def f2c(value):

    c = (value-32)/1.8

    return c

def c2f(value):

    f = (value *(9/5) + 32)

    return f


n = input("Enter the conversion to be done:")

if n == 'c2f':
    i = int(input('Enter the value:'))

    print(c2f(i))

elif n == 'f2c':
    i = int(input('Enter the value:'))

    print(f2c(i))

else:
    print("Invalid Input")"""

n = input("Enter the operation to be done(f2c) or (c2f):")

if n == 'f2c':
    i = float(input("Enter the value:"))
    print("{}°F in °C is :{:.2f}°C".format(i,(i-32)/1.8))

elif n =='c2f':
    i = float(input("Enter the value:"))
    print("{}°F in °C is :{:.2f}°C".format(i,(i*(9/5)+32)))
