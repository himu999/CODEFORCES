t = int(input())

if t % 2 == 0:

    for i in range(3, t + 1):
        a = i
        b = t - i

        if a % 2 == 0 and b % 2 == 0:
            print("YES")
            break
    else:
        print("NO")


else:
    print("NO")
