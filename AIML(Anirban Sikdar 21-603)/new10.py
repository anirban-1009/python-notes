#16-11-2021
#weather the given number is prime or not


n = int(input(">"))
k = True
"""
i=2
while i<=n//2:
    if n%i == 0:
        k = False
        break
    i+=1

if k == True:
    print("prime")

else:
    print("composite")
"""

for i in range(2,(n//2)+1):
    if n%i == 0:
        k = False
        break

if k == True:
    print("prime")
else:
    print("composite")
