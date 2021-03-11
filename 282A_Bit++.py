t = int(input())

X = 0

for i in range(t):
    c = input()
    if c == "++X" or c == "X++":
        X += 1
    elif c == "--X" or c == "X--":
        X -= 1

print(X)





