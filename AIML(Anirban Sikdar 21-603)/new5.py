y = [1,2,"AIML", 7]
print(y[2])
y[2] = "Branch"
print(y)
y.append(99)
print(y)
y.insert(2,88)
print(y)
y.remove(2)
print(y)
print(y.pop())
print(y)
print(y.pop(1))
print(y)
y.remove(y[2])
print(y)
x = [2,3,9,4]
y = [1,2,2]
x.append(y)
print(x[4])
y.extend(x)
print(y)
print(len(y))
print(y[6])
#2-11-2021
