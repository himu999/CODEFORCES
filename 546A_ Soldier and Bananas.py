k, n, w = map(int, input().split())

s = 1

cnt = 0

for i in range(1, w+1):
    s = k * i
    cnt += s


if n < cnt:
    print(cnt - n)
else:
    print("0")
