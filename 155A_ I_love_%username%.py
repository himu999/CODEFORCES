t = int(input())

a = map(int, input().split())
a = list(a)
ln = len(a)

b = []
cont = 0
b.append(a[0])
for i in range(ln):

    min1 = min(b)
    max1 = max(b)

    if i >= 1:

        if a[i] <= min1 or a[i] >= max1:
            if a[i] not in b:
                b.append(a[i])
                cont += 1


print(cont)
