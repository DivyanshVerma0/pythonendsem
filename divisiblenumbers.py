num = int(input("Enter a number till where u want the divisibles: "))

for i in range(1, num + 1):
    if i % 13 == 0:
        print(i)