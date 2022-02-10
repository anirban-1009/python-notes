import re
def getUniqueWords(n):
    uniqueWord = []
    y = re.findall('\S+',n)
    for i in y:
        if i not in uniqueWord:
            uniqueWord.append(i)
        else:
            pass
    return uniqueWord

n=input(">")
print(getUniqueWords(n))
