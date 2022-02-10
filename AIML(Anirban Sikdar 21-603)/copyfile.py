n=input("Enter the source file:")
m=input("Enter the destination file:")

f1 = open(m,'a')

with open(n,'r') as f:
    for i in f.readlines():
        f1.write(i)
        print(i)
    print(f"The contents of {n} are been copied to {m}")

f1.close()
