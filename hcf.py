x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

print(hcf(x, y))