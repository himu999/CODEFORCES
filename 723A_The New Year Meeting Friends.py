lst = map(int, input().split())
lst = list(lst)
minimum = min(lst)
maximum = max(lst)
b = 0

for i in range(3):
    if lst[i] != minimum and lst[i] != maximum:
        b = lst[i]

s = maximum-b
s += b - minimum
print(s)
