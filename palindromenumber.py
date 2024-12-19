def f(num):
    reverse_num = int(str(num)[::-1])
    return reverse_num

number = int(input())
reversed_number = f(number)
if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")