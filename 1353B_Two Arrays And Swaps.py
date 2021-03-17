t = int(input())
a = []
b = []
i = 1

while i <= t:
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for j in range(k):
        a_min = min(a)
        b_max = max(b)
        a_min_index = a.index(a_min)
        b_max_index = b.index(b_max)

        if a_min < b_max:

            temp = a[a_min_index]
            a[a_min_index] = b[b_max_index]
            b[b_max_index] = temp
    print(sum(a))

    i += 1
