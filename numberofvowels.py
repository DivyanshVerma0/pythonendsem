a = input("Enter a string: ")
a = a.casefold()
vowels = "aeiou"

count = {}.fromkeys(vowels, 0)

for char in a:
    if char in count:
        count[char] += 1

print(count)