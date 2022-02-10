#23-11-2021
#write a python program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate weather or not the triangle is a right angle triangle
print("Enter the sides of the triangle:")
a = []
for k in range(1,4):
    i = int(input(">"))
    a.append(i)

a.sort()
#z = max(a)
#a.remove(z)
if (a[2]**2) == (a[0]**2)+(a[1]**2):
    print("It is a right angle triangle")

else:
    print("It is not a right angle triangle")
