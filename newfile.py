import sys
r = str(sys.argv[1])
w = str(sys.argv[2])
f=open(w,'a')
with open(r,'r') as f1:
    for line in f1.readlines():
        f.write(line)


f.close()
