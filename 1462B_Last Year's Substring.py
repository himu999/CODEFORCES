t = int(input())

while t > 0:

    n = int(input())
    s = input()
    a = []
    k = []
    ss = ""

    if n > 3:
        if n == 4:
            if s[0] == '2':
                for i in range(1, n):
                    if s[i - 1] == s[i]:
                        print("NO")
                        break
                else:
                    print("YES")
            else:
                print("NO")
        else:
            for j in range(n):
                if s[j] == "0" or "2":
                    if j < 1:
                        if s[j] == "2":
                            a.append(s[j])
                    elif s[j] != s[j - 1]:
                        a.append(s[j])

                    if j == n-1:
                        for w in range(len(a)):
                            ss += a[w]
                        if ss == "2020":
                            print("YES")
                            break
                        else:
                            print("NO")
                            break
                else:
                    k.append[j]
                    for m in range(len(k)):
                        if k[m + 1] - k[m] > 1:
                            print("NO")
                            break
            else:
                print("YES")

    t -= 1
