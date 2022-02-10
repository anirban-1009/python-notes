class strulta:
    def __init__(self, r):
        self.str = r
    def main(self):
        l = []
        for j in self.str:
            l.append(j)
        l.reverse()
        print(l)
        for m in l:
            print(m,end='')
        print('')
try:
    while True:
        u = input(">>")
        m = strulta(u)
        m.main()
except KeyboardInterrupt:
    print('Cleaning up...')
#reversing string
#04-01-2022
