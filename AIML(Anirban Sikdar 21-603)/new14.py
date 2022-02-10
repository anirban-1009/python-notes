with open('read.txt','w+') as t:#context manager
    t.write("Happy hitam\n")
    t.seek(0)
    a = t.read()
    print(a)

    
a = open('read0.txt','w+')
a.write('Hello\nName is Just a label')
a.seek(0)
print(a.read(7))
a.close()

"""with open('read.txt','a') as m:
    m.write('*******')


with open('read.txt','r') as p:
    print(p.read())

f = open('read.txt','r')
print(f.read())
f.close()
"""

#30-11-2021
