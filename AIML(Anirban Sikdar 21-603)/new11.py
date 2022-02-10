#23-11-2021

n = int(input(">"))


print(f"The prime numbers till {n} are:", end='')
"""while j<=n:
    k =True
    i = 2

    while i <= j//2:
        if j%i ==0:
            k = False
            break
        i+=1

    if k == True:
        print(j, end=',')

    j+=1
"""




for j in range(2, n+1):
    m = True

    for i in range(2, (j//2)+1):
        if j%i == 0:
            m = False
            break 

    if m == True:
        print(j, end=',')
