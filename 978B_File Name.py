a = int(input())
b = input()

count = 0

for i in range(a-2):
    if b[i:i+3] == "xxx":
        count += 1

print(count)