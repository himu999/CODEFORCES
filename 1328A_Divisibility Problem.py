t = int(input())

i = 1
c = []
while i <= t:

    a, b = map(int, input().split())

    cont = 0

    if a % b == 0:
        c.append(cont)
    elif a < b:
        cont = b - a
        c.append(cont)
    else:
        val = a % b
        cont = b - val
        c.append(cont)

    i += 1


for j in range(len(c)):
    print(c[j])
