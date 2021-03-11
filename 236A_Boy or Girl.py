t = input()

b = len(t)
cnt = 0
c = []
for i in range(b):

    if t[i] not in c:
        c.append(t[i])
        cnt += 1

if cnt % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
