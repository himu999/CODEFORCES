t = int(input())

while t > 0:
    count = 0

    a, b = map(int, input().split())

    if a > b:
        a = a - b
        if a % 2 == 0:
            count += 1
        else:
            count += 2
    elif b > a:
        b = b - a
        if b % 2 == 0:
            count += 2
        else:
            count += 1

    print(count)

    t -= 1
