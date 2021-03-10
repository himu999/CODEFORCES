t = int(input())

j = 1

while j <= t:

    string = input()

    d = len(string)

    if d > 10:

        c = len(string[1:d-1])
        print(f"{string[0]}{c}{string[d-1]}")

    else:
        print(string)

    j = j + 1


