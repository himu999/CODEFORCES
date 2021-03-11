limak_w, brother_w = map(int, input().split())

i = 0

while True:
    i += 1
    limak_w = limak_w * 3
    brother_w = brother_w * 2

    if limak_w > brother_w:
        break


print(i)
