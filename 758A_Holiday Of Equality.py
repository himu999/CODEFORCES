t = int(input())

a = map(int, input().split())
a = list(a)
b = max(a)
c = len(a)
summ = 0
if c > 1:
    for i in range(0, c):
        if a[i] < b:
            summ += b - a[i]

print(summ)
