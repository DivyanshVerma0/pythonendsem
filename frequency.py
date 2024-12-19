#dictionary frequency to count frequency of each and print in dictionary
numbers = list(input("Enter numbers separated by spaces: ").split())
frequency_dict = {}
for number in numbers:
    if number in frequency_dict:
        frequency_dict[number] += 1
    else:
        frequency_dict[number] = 1
print(frequency_dict)