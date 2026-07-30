name=str(input("enter your name: "))
if len(name)<3:
    print("name must be 3 chars")
elif len(name)>50:
    print("name can be 50 chars")
else:
    print("name looks good")