#16-11-2021
dic = {1:"one", 2:"two", 3:"three"}

"""for i,j in enumerate(dic.keys(), 66006):
    print(i,j)
for i,(k,v) in enumerate(dic.items(),99):
    print(i,k,v)"""

l = {1,5,9,2}
print(type(l))
"""l.add(29)
print(l)
l.update([1,2,3,4])
print(l)
m = {1,(1,5),8}
#p = {1,[1,5],8}"""

k = {1,8,2}
print(l|k)
print(l&k)
#l.remove(5)
#l.remove(5)
#print(l)
#l.discard(5)
j = {5,7}
print(l.union(k,j))
print(l.intersection(k))
print(l.difference(k))
