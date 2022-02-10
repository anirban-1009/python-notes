"""f = open('test.txt','wb+')
f.write(b'Hello World\nHello India')
f.seek(-3, 1)
print(len(f.read()))
print(f.tell())
print(f.read())
"""
for i in range(1,6):
    print("*"*i)
    if i == 5:
        for i in range(4,0,-1):
            print("*"*i)
