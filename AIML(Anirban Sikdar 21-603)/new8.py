n=int(input(">"))
i = 0
j= 1
"""
while i<n:
    i,j=i+j,i
    print(j,end=",")


"""#fibonacci series
x =1
"""
for i in range(1,n+1):
    x = x*i

print(f"{n}!={x}")
"""#for loop
"""
while j<=n:
    x,j = x*j,j+1
print(x)
"""#while loop
