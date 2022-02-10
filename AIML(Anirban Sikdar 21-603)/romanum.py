class Py_sol:
    def int_to_roman(self, num):
        val = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,
            1
            ]
        syb = [
            "M","CM","D","CD",
            "C","XC","L","XL",
            "X","IX","V","IV",
            "I"
            ]
        roman_num=""
        i=0
        while num>0:
            for _ in range(num//val[i]):
                roman_num+=syb[i]
                num-=val[i]
            i+=1
        return roman_num

    def powr(self, x,n):
        if x ==0 or x==1 or n==1:
            return x

        elif x<0:
            return 1/self.powr(x,-n)

        elif n==0:
            return 1

        else:
            return x**n

print(Py_sol().powr(9,-8))
