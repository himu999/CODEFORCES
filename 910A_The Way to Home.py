n, d = map(int, input().split())

strng = input()
z_count = 0
z_jump = 0
fl = 0

if strng[0] != '1' or strng[n - 1] != '1':
    print(-1)

else:
    for i in range(n):
        if strng[i] == "0":
            fl += 1
            if fl >= d:
                print(-1)
                break
        else:
            fl = 0
    else:
        while z_jump < n - 1:
            if len(strng[z_jump:]) <= d:
                z_count += 1
                break
            else:
                if strng[d + z_jump] == "1":
                    z_jump += d
                    z_count += 1
                else:
                    for j in range(d + z_jump, z_jump, -1):
                        if strng[j] == "1":
                            z_jump = j
                            z_count += 1
                            break

        print(z_count)
