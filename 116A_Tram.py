t = int(input())
i = 0
passenger = 0
maximum = 0
while i < t:
    a, b = map(int, input().split())
    if i == 0:
        passenger = b
        maximum = b
    else:
        passenger += (b - a)
        if passenger > maximum:
            maximum = passenger
    i += 1

print(maximum)
