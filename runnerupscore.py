n = (input("Enter the numbers: "))
runnerup = list(map(int, n.split()))

sorted_list = sorted(set(runnerup), reverse=True)
if len(sorted_list) > 1:
    final = sorted_list[1]

print(final)
