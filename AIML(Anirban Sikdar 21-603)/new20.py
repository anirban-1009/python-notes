#ex17
import re
with open('sample.txt') as f:
    txt = f.read()
    k = re.findall('\S+',txt)
m = []
for i in k:
    if i not in m:
        m.append(i)
    else:
        pass
m.sort()
print(m)
#4-01-22
