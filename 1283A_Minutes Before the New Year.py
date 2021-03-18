t = int(input())
i = 1
while i <= t:
    a, b = map(int, input().split())
    summ = (23 - a) * 60 + (60 - b)

    print(summ)

    i += 1
