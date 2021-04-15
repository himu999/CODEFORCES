n = int(input())
summation = 0
a = []
for i in range(1, n+1):
    if i == 1:
        a.append(1)

    k = 4 * (i-1)
    a.append(k)

summation = sum(a)
print(summation)