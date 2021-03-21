n, m = map(int, input().split())
count = 0
for i in range(1, n+1):

    if i % 2 != 0:
        for j in range(m):
            print("#", end="")
        print()
    else:
        count += 1
        if count % 2 != 0:
            for k in range(m-1):
                print(".",end="")
            print("#")

        else:
            print("#", end="")

            for k in range(1,m):
                print(".", end="")
            print()

