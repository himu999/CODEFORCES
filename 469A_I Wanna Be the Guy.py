n = int(input())
lst = []
s = "I become the guy."
for i in range(1, n+1):
    lst.append(i)

lst2 = map(int, input().split())
lst2 = list(lst2)

lst3 = map(int, input().split())
lst3 = list(lst3)

lst4 = lst2[1:] + lst3[1:]

for j in range(n):
    if lst[j] not in lst4:
        s = "Oh, my keyboard!"
        break

print(s)
