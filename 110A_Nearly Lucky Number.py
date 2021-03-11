a = input()
b = len(a)

cnt = 0

for i in range(b):
    if "4" in a[i] or "7" in a[i]:

        cnt += 1

if b > 1 and 0 < cnt < 8:
    if cnt % 4 == 0 or cnt % 7 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
