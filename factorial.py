num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")

if num == 0:
    print("The factorial of 0 is" , 1)

if num > 0 :
    for i in range(1, num + 1):
        fact = fact * i

    print("The factorial of", num, "is", fact)