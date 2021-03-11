n = int(input())
t = input()
b = len(t)
cnt = 0

for i in range(1, b):

    if t[i-1] == t[i]:
        cnt += 1
print(cnt)
