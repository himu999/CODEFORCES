t = int(input())

while t > 0:
    n = int(input())
    temp = 0

    if n >= 2020:
        if n % 2020 == 0 or n % 2021 == 0:
            print("YES")
        else:
            while True:
                if n >= 2020:
                    n -= 2021
                    if n % 2020 == 0:
                        print("YES")
                        break
                else:
                    print("NO")
                    break
    else:
        print("NO")
    t -= 1
