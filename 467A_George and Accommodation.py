t = int(input())
count = 0
while t > 0:

    a, b = map(int, input().split())

    c = b - a

    if c >= 2:
        count += 1

    t -= 1

print(count)
