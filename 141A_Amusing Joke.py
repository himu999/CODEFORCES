a = input()
b = input()
c = input()

a = a + b
a = list(a)
a.sort()
c = list(c)
c.sort()

if len(a) == len(c):
    if a == c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
