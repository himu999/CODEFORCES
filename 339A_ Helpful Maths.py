k = input()
c = ""
t = list(k)
b = len(t)

for i in range(b):
    for j in range(0, b, 2):

        if j+2 < b:
            if t[j] > t[j + 2]:
                temp = t[j]

                t[j] = t[j + 2]

                t[j + 2] = temp

for l in range(b):
    c += t[l]

print(c)
