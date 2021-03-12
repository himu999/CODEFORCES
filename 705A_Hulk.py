a = "I hate that "
b = "I love that "
s = ""
n = int(input())

if n > 1:
    for i in range(1, n + 1):

        if i == n:
            if i % 2 == 0:
                s += "I love it"
            else:
                s += "I hate it"
        else:
            if i % 2 == 0:
                s += b
            else:
                s += a


else:
    s += "I hate it"

print(s)
