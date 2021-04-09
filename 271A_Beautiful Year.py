year = int(input())
y = ""
year += 1
while True:
    s_y = str(year)
    lst = list(s_y)
    d = len(s_y)

    for i in range(1, d):
        if i == 1:
            if lst[i] == lst[i-1]:
                year += 1
                break
        else:
            if lst[i] in lst[0:i]:
                year += 1
                break
    else:
        y = "YES"

    if y == "YES":
        print(year)
        break
