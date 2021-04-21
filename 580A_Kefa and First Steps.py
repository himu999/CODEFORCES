n = int(input())
lst = [*map(int, input().split())]
count = 1
temp = 0

for i in range(1, n):
    if lst[i] >= lst[i-1]:
        count += 1
    else:
        if temp <= count:
            temp = count
        count = 1

if temp <= count:
    temp = count

print(temp)
