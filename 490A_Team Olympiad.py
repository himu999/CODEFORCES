t = int(input())

a = map(int, input().split())
a = list(a)

a_1 = []
a_2 = []
a_3 = []

for i in range(t):
    if a[i] == 1:
        a_1.append(i)
    elif a[i] == 2:
        a_2.append(i)
    else:
        a_3.append(i)

d1 = len(a_1)
d2 = len(a_2)
d3 = t - (d1 + d2)


minn = min(d1, d2, d3)
print(minn)
for k in range(minn):
    print(a_1[k]+1, a_2[k]+1, a_3[k]+1)
