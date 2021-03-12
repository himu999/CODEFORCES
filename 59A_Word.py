string = input()
upper = 0
lower = 0

i = 0

while i < len(string):

    if string[i].isupper():
        upper += 1
    elif string[i].islower():
        lower += 1
    i += 1

if upper > lower:
    print(string.upper())
else:
    print(string.lower())
