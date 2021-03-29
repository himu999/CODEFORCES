t = int(input())

while t > 0:
    flag = 1
    num = input()
    lst = list(num)
    num = int(num)
    summ = 0

    for j in range(len(lst)):
        summ += int(lst[j])




    while True:
        for n in range(2, summ+1):
            if num % n == 0 and summ % n == 0:
                flag = 2
                break
        else:
            summ = 0
            num += 1
            lst = list(str(num))
            for j in range(0, len(lst)):
                summ += int(lst[j])

        if flag > 1:
            break
    print(num)


    t = t - 1
