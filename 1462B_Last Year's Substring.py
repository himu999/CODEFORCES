t = int(input())

while t > 0:

    n = int(input())
    s = input()

    if s[:4] == "2020":
        print("YES")
    elif s[:3] == "202" and s[n - 1:] == "0":
        print("YES")
    elif s[:2] == "20" and s[n - 2:] == "20":
        print("YES")
    elif s[:1] == "2" and s[n - 3:] == "020":
        print("YES")
    elif s[n - 4:] == "2020":
        print("YES")
    else:
        print("NO")

    t -= 1
