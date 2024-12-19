punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter a string: ")

no_punc = ""

for i in string:
    if i not in punc:
        no_punc += i

print(no_punc)


