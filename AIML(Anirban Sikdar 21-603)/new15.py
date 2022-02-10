print("Enter the file location to be copied from one to other")

a = str(input('From:'))
b = str(input('To:'))


with open(a,'r') as a:
    text = a.read()
    print("The content to be copied:\n",text)
    input("Enter to continue or press Ctrl+C to cancel:")


with open(b,'w') as b:
    b.write(text)
    print("The file is successfully overwritten")
#30-11-2021
