"""import re
txt = "The hat is on the mat"
k = re.findall("at",txt)
print(k)
k = re.search("at",txt)
print(k.start())
k = re.split(" ",txt)
print(k)
print(len(k))
k = re.split('at',txt,2)
print(k)
k = re.sub(" ","k",txt,2)
print(k)
"""

import re
txt = "Welcome to Hitam.org"
k = re.search('\.',txt)
print(k.start(),k.end())
k = re.findall("Hi..m",txt)
print(k)
#txt = r"my number is \n"-->raw text
txt = 'my number is 12345'
k = re.findall('\d+',txt)
print(k)
k = re.findall('\D+',txt)
print(k)
print(re.findall('\S+',txt))
#21-12-21
