def isPalindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
ans = isPalindrome(s)

if ans:
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a Palindrome")