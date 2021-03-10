string = input()

a = ""

for i in range(len(string)):
    if i == 0:
        c = string[i].capitalize()
        a += c
    else:
        a += string[i]

print(a)
