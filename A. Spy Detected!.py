t = int(input())

while t > 0:
    n = int(input())

    a = map(int, input().split())
    a = list(a)

    for i in range(n):
        if a[i] not in a[i+1:] and a[i] not in a[:i]:
            print(i+1)
            break
    t -= 1