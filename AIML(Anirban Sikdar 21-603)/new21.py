def romdec(i):
    if i in range(11):
        if i < 4:#till 3
            for m in range(i):
                print('I', end='')
            print('')
        elif i in range(4, 9):#from 4 to 8
            if i==4:#4
                print('I', end='')
                print('V')
            else:# greater or equal to 5
                print('V', end='')
                if i == 5:
                    print('')
                elif i >5:# greater than 5
                    k = i-5
                    for m in range(k):
                        print('I',end='')
                    print('')
                else:
                    pass
        else:
            if i == 9:
                print('IX')
            else:
                print('X')
    elif i == 0:
        print('')

def rombdec(i):
    if i in range(11,110):
        k = i//10
        if k<=3:#less than or equal to 39
            for l in range(k):
                print('X',end='')
            romdec(i%10)
        elif k in range(4, 9):#in range of 40 to 89
            if k==4:
                print('XL',end='')
                romdec(i%10)
            else:
                print('L',end='')
                if k == 5:
                    romdec(i%10)
                else:
                    z = k-5
                    for r in range(z):
                        print('X', end='')
                    romdec(i%10)
        else:
            if k ==9:#from 90 to 99
                print('XC', end='')
                romdec(i%10)
            else:#from 100 to 109
                print('C', end='')
                romdec(i%10)                
try:
    while True:
        i = int(input(">"))
        rombdec(i)
except KeyboardInterrupt:
    print("cleaning...")
except Exception as e:
    print(e)
    print("cleaning...")
#04-01-2022
#int to roman numeral
