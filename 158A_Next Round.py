a, b = map(int, input().split())

lst = map(int, input().split())

d = list(lst)
c = len(d)
cnt = 0

for i in range(c):
    if d[i] > 0:
        if d[i] >= d[b - 1]:
            cnt += 1

print(cnt)
