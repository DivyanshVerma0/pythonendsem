def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)
a = int(input("Enter a number: "))
print(fact(a))