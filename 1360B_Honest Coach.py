t = int(input())

while t > 0:
    a = int(input())
    b = list(map(int, input().split()))
    b.sort()
    c = []

    for i in range(1, len(b)):
        d = max(b[i], b[i-1]) - min(b[i], b[i-1])
        c.append(d)

        if d == 0:
            break
    print(min(c))

    t -= 1
