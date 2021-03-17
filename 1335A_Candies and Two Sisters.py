t = int(input())

i = 1

while i <= t:

    a = int(input())

    if a <= 2:
        print(0)
    elif a % 2 != 0:
        b = a // 2
        print(b)
    else:

        b = a // 2
        b -= 1
        print(b)

    i += 1
