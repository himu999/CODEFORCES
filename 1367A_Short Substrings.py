t = int(input())

while t > 0:
    string = input()
    b = len(string)
    a = ""
    for i in range(0, b, 2):
        a += string[i]
    a += string[b-1]

    print(a)
    t -= 1
