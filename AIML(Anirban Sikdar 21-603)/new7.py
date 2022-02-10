m = int(input(">"))
n = int(input(">"))
o = int(input(">"))

avg = (m+n+o)/3

"""if avg>=70:
    print("Distinction")

elif avg>=60:
    print("First Class")

elif avg>=50:
    print("second Class")

else:
    print("Fail")

"""

"""
if avg>=70:
    print("Distinction")
else:
     if avg>=60:
         print("First Class")
     else:
        if avg>=50:
            print("Second Class")

        else:
            print("Fail")
        
"""

if avg>=70:
    print("Distinction")

if avg<70 and avg>=60:
    print("First Class")

if avg<60 and avg>=50:
    priht("Second Class")
if avg<50:
    print("Failed = %d"%(avg))

print(f"TOTAL MARKS = {m+n+o}|AVERAGE = {avg}|marks per subject = {m}% {n}% {o}%")
