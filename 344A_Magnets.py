t = int(input())
i = 0
cnt = 0
a = []
while i < t:

    inp = input()

    if len(a) == 0:
        cnt += 1
        a.append(inp)

    else:
        a.append(inp)
        if a[i-1] != a[i]:
            cnt += 1

    i += 1

print(cnt)
