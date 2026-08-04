try:
    age=int(input("age:"))
    print(age)
except ValueError as e:
    print(e)