class Aiml:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y


class Hitm(Aiml):
    def message(self, msg):
        return "Hello " + str(msg) + "!!!!"

k = Hitm(2,9)
print(k.add())
print(k.message("India"))
#21-12-21
