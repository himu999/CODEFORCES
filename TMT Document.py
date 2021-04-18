t = int(input())

while t > 0:

    n = int(input())
    str1 = input()
    number_t = 0
    number_m = 0
    count = 0
    flag = "NO"

    for i in range(n):
        if str1[i] == "T":
            number_t += 1
        else:
            number_m += 1

    if number_t == 2*number_m:
        for j in range(n):
            if str1[j] == "T":
                count += 1
            else:
                count -= 1
            if count < 0:
                print("NO")
                break
        else:
            flag = "YES"
            count = 0

        if flag=="YES":
            for k in range(n - 1, -1, -1):
                if str1[k] == "T":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    print("NO")
                    break
            else:
                print("YES")

    else:
        print("NO")
    t -= 1
