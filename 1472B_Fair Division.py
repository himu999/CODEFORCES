t = int(input())

i = 1

while i <= t:

    n = int(input())
    lst = list(map(int, input().split()))
    b = n // 2

    if n % 2 == 0:
        if sum(lst[:b]) == sum(lst[b:]):
            print("YES")
        elif sum(lst) % 2 == 0:
            print("YES")
        else:
            print("NO")

    else:
        if sum(lst) % 2 == 0:
            if lst[:] == lst[n - 1:-1]:
                print("NO")
            elif sum(lst[:b]) == sum(lst[b:]):
                print("YES")
            else:
                summ = sum(lst) % n
                if summ % 2 != 0:
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")

    i += 1
