t = int(input())
i = 0
cnt = 0
while i < t:

    summation = 0
    lst = list(map(int, input().split()))

    for j in range(len(lst)):
        summation += lst[j]

    if summation >= 2:
        cnt += 1

    i += 1

print(cnt)
