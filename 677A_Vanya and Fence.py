n, h = map(int, input().split())

lst = map(int, input().split())
lst = list(lst)
count = 0

for i in range(n):
    if lst[i] > h:
        count += 2
        continue
    count += 1
print(count)
