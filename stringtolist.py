x = (input("enter your numbers:"))

lst = list(map(int, x.split()))

diff = max(lst) - min(lst)
print(diff)